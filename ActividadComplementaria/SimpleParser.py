# Generated from Simple.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,4,1,20,8,1,11,1,12,1,21,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,61,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,69,8,4,10,4,12,
        4,72,9,4,1,4,0,1,8,5,0,2,4,6,8,0,1,1,0,9,10,77,0,11,1,0,0,0,2,15,
        1,0,0,0,4,37,1,0,0,0,6,47,1,0,0,0,8,60,1,0,0,0,10,12,3,2,1,0,11,
        10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,
        0,15,16,5,1,0,0,16,17,5,12,0,0,17,19,5,2,0,0,18,20,3,4,2,0,19,18,
        1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,
        23,24,5,3,0,0,24,3,1,0,0,0,25,26,5,4,0,0,26,27,5,12,0,0,27,38,5,
        5,0,0,28,29,5,4,0,0,29,30,5,12,0,0,30,31,5,6,0,0,31,32,5,12,0,0,
        32,33,5,7,0,0,33,34,5,2,0,0,34,35,3,6,3,0,35,36,5,3,0,0,36,38,1,
        0,0,0,37,25,1,0,0,0,37,28,1,0,0,0,38,5,1,0,0,0,39,40,3,8,4,0,40,
        41,5,5,0,0,41,48,1,0,0,0,42,43,5,12,0,0,43,44,5,8,0,0,44,45,3,8,
        4,0,45,46,5,5,0,0,46,48,1,0,0,0,47,39,1,0,0,0,47,42,1,0,0,0,48,7,
        1,0,0,0,49,50,6,4,-1,0,50,61,5,11,0,0,51,52,5,12,0,0,52,53,5,6,0,
        0,53,54,5,11,0,0,54,61,5,7,0,0,55,61,5,12,0,0,56,57,5,6,0,0,57,58,
        3,8,4,0,58,59,5,7,0,0,59,61,1,0,0,0,60,49,1,0,0,0,60,51,1,0,0,0,
        60,55,1,0,0,0,60,56,1,0,0,0,61,70,1,0,0,0,62,63,10,6,0,0,63,64,7,
        0,0,0,64,69,3,8,4,7,65,66,10,5,0,0,66,67,7,0,0,0,67,69,3,8,4,6,68,
        62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,
        0,71,9,1,0,0,0,72,70,1,0,0,0,7,13,21,37,47,60,68,70
    ]

class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'int'", "';'", 
                     "'('", "')'", "'='", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "ID", 
                      "WS" ]

    RULE_prog = 0
    RULE_classDef = 1
    RULE_member = 2
    RULE_stat = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "classDef", "member", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INT=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ClassDefContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SimpleParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.classDef()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.MemberContext)
            else:
                return self.getTypedRuleContext(SimpleParser.MemberContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)




    def classDef(self):

        localctx = SimpleParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(SimpleParser.T__0)
            self.state = 16
            self.match(SimpleParser.ID)
            self.state = 17
            self.match(SimpleParser.T__1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.member()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 23
            self.match(SimpleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.ID)
            else:
                return self.getToken(SimpleParser.ID, i)

        def stat(self):
            return self.getTypedRuleContext(SimpleParser.StatContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = SimpleParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(SimpleParser.T__3)
                self.state = 26
                self.match(SimpleParser.ID)
                self.state = 27
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(SimpleParser.T__3)
                self.state = 29
                self.match(SimpleParser.ID)
                self.state = 30
                self.match(SimpleParser.T__5)
                self.state = 31
                self.match(SimpleParser.ID)
                self.state = 32
                self.match(SimpleParser.T__6)
                self.state = 33
                self.match(SimpleParser.T__1)
                self.state = 34
                self.stat()
                self.state = 35
                self.match(SimpleParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)


        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SimpleParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(SimpleParser.ID)
                self.state = 43
                self.match(SimpleParser.T__7)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(SimpleParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimpleParser.INT, 0)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ExprContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(SimpleParser.INT)
                pass

            elif la_ == 2:
                self.state = 51
                self.match(SimpleParser.ID)
                self.state = 52
                self.match(SimpleParser.T__5)
                self.state = 53
                self.match(SimpleParser.INT)
                self.state = 54
                self.match(SimpleParser.T__6)
                pass

            elif la_ == 3:
                self.state = 55
                self.match(SimpleParser.ID)
                pass

            elif la_ == 4:
                self.state = 56
                self.match(SimpleParser.T__5)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(SimpleParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SimpleParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(6)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




