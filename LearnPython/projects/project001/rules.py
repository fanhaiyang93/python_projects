#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 19:04
# @Author  : fanhaiyang
# @File    : rule.py
# @Software: PyCharm Community Edition
# @comment : 规则，在主程序（分析器）中使用，主程序要决定对给定的块使用什么样的规则，让每个规则对块做需要的转换
# 换句话说，规则要：能识别自己适用于哪种块（条件）；能对块进行转换（操作）。因此每个规则对象都有两个方法：condition和action
# Condition方法需要一个参数--所涉及的块，它返回一个布尔值来表示规则是否适用于给定的块

class Rule:
    '''
    所有规则的超类
    '''

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    a heading is a single line that is at most 70 characters and
    that doesn't end with a colon
    """
    type = 'heading'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    """
    The title is the first block in the document,provided that it is a heading
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: return False  # title只有一个，第一次匹配成功后，修改标记，其他的块都不会匹配成功
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    A list item is a paragraph that begins with a hyphen(连字符）.
    As part of the formatting,the hyphen is removed.(去掉连字符）
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True  # 表示结束块的规则处理


class ListRule(ListItemRule):
    """
    A list begins between a block that is not a list item and a subsequent(之后的）list item.
    It ends after the last consecutive(连贯的） list item.
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):  # 如果是listItem，start，只执行一次
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):  # 如果不是listItem，end，也只执行一次
            handler.end(self.type)
            self.inside = False
        return False  # 表示不结束块的规则处理


class ParagraphRule(Rule):
    """
    A paragraph is simply a block that isn't covered by any of the other rules.
    """
    type = 'paragraph'

    def condition(self, block):
        return True
