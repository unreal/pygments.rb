# -*- coding: utf-8 -*-
"""
    pygments.lexers.onerobotics
    ~~~~~~~~~~~~~~~~~~~

    Custom lexers for ONE Robotics Company

    :copyright: Copyright 2014 by ONE Robotics Company LLC
    :license: BSD, see LICENSE for details.
"""
import re

from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, \
    using, DelegatingLexer
from pygments.token import Text, Name, Number, String, Comment, Punctuation, \
     Other, Keyword, Operator, Literal, Whitespace

__all__ = ['TpLexer']

class TpLexer(RegexLexer):
  """
  For `FANUC TP <http://fanucrobotics.com>`_ source code.
  """

  name = 'TP'
  aliases = ['tp', 'tpp', 'tpe']
  filenames = ['*.ls']

  keywords = [
      'CALL', 'IF', 'JMP', 'STOP_TRACKING', 'STOP', 'START', 'RESET', 'WAIT'
  ]

  motion_modifiers = [
      'ACC', 'AP_LD', 'CNT', 'Offset', 'RT_LD', 'TA', 'TB', 'VOFFSET'
  ]

  tokens = {
      'root': [
          (r'  ![^;]*', Comment),
          (r'"[^"]*"', String),
          (r'(\/PROG|\/ATTR|\/APPL|\/MN|\/POS|\/END)', Keyword.Declaration),
          (r'(ON|OFF)', Keyword.Pseudo),
          (r'(L|J|C) (?=P)', Keyword.Reserved),
          (r'max_speed', Keyword.Reserved),
          (r'sec', Keyword.Reserved),
          (r'^\s+\d+:\s+', Punctuation),
          (r'[:;()\[\]]', Punctuation),
          (r'\s+', Text),
          (r'(%s)\b' % "|".join(keywords), Keyword),
          (r'LBL', Name.Label),
          (r'(AR|R|PR|TIMER|DI|DO|F|RI|RO|UI|UO|SI|SO|GI|GO|SR|VR)(?=\[)', Keyword.Type, 'type'),
          (r'(OWNER|ASCBIN|COMMENT|PROG_SIZE|CREATE|DATE|TIME_SLICE|MODIFIED|FILE_NAME|'
           r'VERSION|LINE_COUNT|MEMORY_SIZE|PROTECT|READ_WRITE|TCD|STACK_SIZE|'
           r'TASK_PRIORITY|TIME|BUSY_LAMP_OFF|ABORT_REQUEST|PAUSE_REQUEST|'
           r'DEFAULT_GROUP|CONTROL_CODE|LINE_TRACK_SCHEDULE_NUMBER|LINE_TRACK_BOUNDARY_NUMBER|'
           r'LINE_TRACK|CONTINUE_TRACK_AT_PROG_END)',
           Keyword.Constant),
          (r'(%s)' % "|".join(motion_modifiers), Keyword),
          (r'\/\/[^;]*', Comment),
          (r'[*=><+-/%!]', Operator),
          (r'(DIV|MOD)', Operator),
          (r'\d+', Number.Integer),
          (r'[a-zA-Z0-9_]+', Name),
          (r'\$', Name.Variable.Global, 'sysvar')
      ],
      'type': [
          (r'[\[:]', Punctuation),
          (r'\d+', Number.Integer),
          (r'[\w _\d]+', Name.Variable),
          (r'\]', Punctuation, '#pop')
      ],
      'sysvar': [
        (r'[\.\[\]]', Punctuation),
        (r'\w+', Name.Variable),
        (r'\d+', Number.Integer),
        (r'\$', Name.Variable.Global),
        (r'\s+', Text, '#pop')
      ]
  }
