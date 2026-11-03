"""验证无连接草稿可保留，并继续检查来源和人审状态。"""

from pathlib import Path
import runpy
import unittest


CHECK = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "check_card.py"))["check_text"]
CARD = '''---
status: draft
author: ai
sources: ["用户提供的课堂记录"]
---
# 延迟反馈可能增加纠错成本

课堂练习如果到期末才收到反馈，学生可能在后续练习中重复同一错误。及时反馈可以提供较早的纠错机会，实际效果还取决于反馈内容与练习安排。下一步检索主题：反馈时机与自主纠错。
'''


class CardTests(unittest.TestCase):
    def test_unlinked_draft_is_not_an_error(self):
        result = CHECK(CARD)
        self.assertEqual((result["links"], result["errors"], result["warnings"]), (0, 0, 0))
        self.assertTrue(any(i["rule"] == "无连接" and i["level"] == "INFO" for i in result["issues"]))

    def test_date_does_not_become_a_link(self):
        result = CHECK(CARD + "\n记录时间为 2024/12，样本比例为 3/4。")
        self.assertEqual(result["links"], 0)

    def test_ai_cannot_be_marked_reviewed_without_human_review(self):
        result = CHECK(CARD.replace("status: draft", "status: reviewed"))
        self.assertTrue(any(i["rule"] == "AI/外部卡未经人审就升级" and i["level"] == "ERROR" for i in result["issues"]))

    def test_missing_source_remains_visible(self):
        result = CHECK(CARD.replace('["用户提供的课堂记录"]', "[]"))
        self.assertTrue(any(i["rule"] == "缺少 sources" for i in result["issues"]))

    def test_resolvable_reference_is_only_a_review_hint(self):
        result = CHECK(CARD + "\n先定义间隔复习为隔开练习时点。这个方法的适用间隔仍需核对材料。")
        self.assertEqual(result["errors"], 0)
        self.assertTrue(any("指示代词" in i["rule"] for i in result["issues"]))

    def test_attribution_does_not_force_removing_the_source(self):
        result = CHECK('# A disputed claim\n\nThe author argues that immediate feedback always improves transfer. This claim needs evidence about the task and timing before it can support a general recommendation.\n', lang="en")
        self.assertEqual(result["errors"], 0)
        hints = [i for i in result["issues"] if i["rule"] == "Source dependence"]
        self.assertEqual(len(hints), 1)
        self.assertEqual(hints[0]["level"], "WARN")

    def test_short_precise_card_is_not_an_error(self):
        result = CHECK('# 有界不蕴含收敛\n\n序列 (-1)^n 有界但不收敛。')
        self.assertEqual(result["errors"], 0)
        self.assertTrue(any(i["rule"] == "内容过短" and i["level"] == "INFO" for i in result["issues"]))

    def test_length_alone_does_not_require_splitting(self):
        # 构造超长正文，只检查长度阈值不再成为拆卡指令。
        result = CHECK('# 推导说明\n\n' + '在给定条件下展开推导。' * 60)
        hints = [i for i in result["issues"] if i["rule"] == "篇幅过长"]
        self.assertEqual(len(hints), 1)
        self.assertEqual(hints[0]["level"], "INFO")
        self.assertEqual(result["errors"], 0)


if __name__ == "__main__":
    unittest.main()
