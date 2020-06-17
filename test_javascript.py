"""    
    test_domonic 
    ~~~~~~~~~~~~~~~~
    
    unit tests for domonic
    
    # TODO - need to do a js call on the same function. get result. compare to ours
    # TODO - test raising value errors
    # TODO - seperate test file per class

"""

import unittest
# import requests
# from mock import patch

from domonic.javascript import Math
from domonic.javascript import Global
from domonic.javascript import Window
from domonic.javascript import Date

# from domonic.javascript import *

from domonic import domonic


class domonicTestCase(unittest.TestCase):

    # domonic.javascript.Math

    def test_domonic_abs(self):
        self.assertEqual( 100, Math.abs(-100.0) )
    
    def test_domonic_LN2(self):
        print("test_domonic_LN2:::")
        print( Math.LN2 )

    def test_domonic_LOG2E(self):
        print("test_domonic_LOG2E:::")
        print( Math.LOG2E )

    def test_domonic_LOG10E(self):
        print("test_domonic_LOG10E:::")
        print( Math.LOG10E )

    def test_domonic_PI(self):
        print("test_domonic_PI:::")
        print( Math.PI )

    def test_domonic_SQRT1_2(self):
        print("test_domonic_SQRT1_2:::")
        print( Math.SQRT1_2 )
            
    def test_domonic_SQRT2(self):
        print("test_domonic_SQRT2:::")
        print( Math.SQRT2 )

    def test_domonic_acos(self):
        print("test_domonic_acos:::")
        # print( Math.acos(-100) ) # TODO - fails numbers greater than 1 or lower than -1 - raise Error?
        print( Math.acos(0.5) )

    def test_domonic_acosh(self):
        print("test_domonic_acosh:::")
        # print( Math.acosh(-100) ) # TODO - fails under zero - rause error?
        print( Math.acosh(100) )

    def test_domonic_asin(self):
        print("test_domonic_asin:::")
        # print( Math.asin(-100) ) # TODO - fails numbers greater than 1 or lower than -1 - raise Error?
        print( Math.asin(0.5) ) 

    def test_domonic_asinh(self):
        print("test_domonic_asinh:::")
        print( Math.asinh(-100) )

    def test_domonic_atan(self):
        print("test_domonic_atan:::")
        print( Math.atan(-100) )

    def test_domonic_atan2(self):
        print("test_domonic_atan2:::")
        print( Math.atan2(-100,100) )

    def test_domonic_atanh(self):
        print("test_domonic_atanh:::")
        # print( Math.atanh(-100) ) # TODO - fails numbers greater than 1 or lower than -1 - raise Error?
        print( Math.atanh(0.5) )

    def test_domonic_cbrt(self):
        print("test_domonic_cbrt:::")
        # print( Math.cbrt(-100) ) # TODO - fails on negative numbers - raise Error?
        print( Math.cbrt(100) )

    def test_domonic_ceil(self):
        print("test_domonic_ceil:::")
        print( Math.ceil(-100) )

    def test_domonic_cos(self):
        print("test_domonic_cos:::")
        print( Math.cos(-100) )

    def test_domonic_cosh(self):
        print("test_domonic_cosh:::")
        print( Math.cosh(-100) )

    def test_domonic_E(self):
        self.assertEqual( 2.718281828459045, Math.E )

    def test_domonic_exp(self):
        print("test_domonic_exp:::")
        print( Math.exp(-100) )

    def test_domonic_floor(self):
        print("test_domonic_floor:::")
        print( Math.floor(-100) )

    def test_domonic_LN10(self):
        self.assertEqual( 2.302585092994046, Math.LN10 )

    def test_domonic_log(self):
        print("test_domonic_log:::")
        # print( Math.log(-100,100) ) # TODO - fails on negative numbers - raise Error?
        print( Math.log(100,10) )
        
    def test_domonic_max(self):
        print("test_domonic_max:::")
        print( Math.max(-100,100) )

    def test_domonic_min(self):
        print("test_domonic_min:::")
        print( Math.min(-100,100) )

    def test_domonic_random(self):
        print("test_domonic_random:::")
        print( Math.random() )

    def test_domonic_round(self):
        print("test_domonic_round:::")
        print( Math.round(-100) )
        
    def test_domonic_pow(self):
        print("test_domonic_pow:::")
        print( Math.pow(100,10) )

    def test_domonic_sin(self):
        print("test_domonic_sin:::")
        print( Math.sin(-100) )

    def test_domonic_sinh(self):
        print("test_domonic_sinh:::")
        print( Math.sinh(-100) )

    def test_domonic_sqrt(self):
        print("test_domonic_sqrt:::")
        # print( Math.sqrt(-100) ) # TODO - fails on negative numbers - raise Error? check js behaviour
        print( Math.sqrt(100) )

    def test_domonic_tan(self):
        print("test_domonic_tan:::")
        print( Math.tan(-100) )

    def test_domonic_tanh(self):
        print("test_domonic_tanh:::")
        print( Math.tanh(-100) )

    def test_domonic_trunc(self):
        print("test_domonic_trunc:::")
        print( Math.trunc(-100) )

    # def test_domonic_math_test(self):
    #   print("test_domonic_math_test:::")
    #   print( Math.abs(-100)*Math.random()*10 )


    # domonic.javascript.Global
    
    def test_domonic_isNaN(self):
        self.assertEqual(True, Global.isNaN("yo"))
        self.assertEqual(False, Global.isNaN(1))

    def test_domonic_Number(self):
        self.assertEqual(1, Global.Number(1))
        self.assertEqual("NaN", Global.Number("test"))
        self.assertEqual(2, Global.Number("1") + Global.Number("1.0"))

    def test_domonic_window_console_log(self):
        # window = Window()
        Window().console.log("test this")

    def test_domonic_window_alert(self):
        # Window().alert("test this 2")
        window = Window()
        window.alert("test this 2")

    def test_domonic_window_document_baseURI(self):
        # Window().alert("test this 2")
        # window = Window()
        # window.alert("test this 2")
        # print(window.document.baseURI)
        # window.document.baseURI = "eventual.technology"
        # print("=",window.document.baseURI)
        
        pass

    '''
    def test_domonic_window_location(self):
        # Window().alert("test this 2")
        window = Window()
        # window.alert("test this 2")
        print("window.location")
        print(window.location)
        window.location = "eventual.technology"
        print("window.location.uri")
        print(window.location)
        print(str(window.location))
        print(window.location.href)
    '''


    def test_domonic_global_encodeURIComponent(self):

        msg = "Test encoding this string! 123 aweseome"
        enc_msg = Global.encodeURIComponent(msg)
        print( enc_msg )
        # print( Global.decodeURIComponent(bytes(enc_msg, encoding="UTF-8")))
        print( Global.decodeURIComponent(enc_msg) )

        # Window().alert("test this 2")
        # window = Window()
        # window.alert("test this 2")
        # print(window.document.baseURI)
        # window.document.baseURI = "eventual.technology"
        # print("=",window.document.baseURI)        
        pass


    def test_javascript_date(self):

        print( "test_javascript_date:::::::::::::::::::::::::::" )
        d = Date()

        print( d.getDate() )
        print( d.getDay() )

        print( d.getFullYear() )
        print( d.getHours() )
        print( d.getMilliseconds() )
        print( d.getMinutes() )
        print( d.getMonth() )
        print( d.getSeconds() )
        print( d.getTime() )
        # print( d.getTimezoneOffset() )
        print( d.getUTCDate() )
        print( d.getUTCDay() )
        print( d.getUTCFullYear() )
        print( d.getUTCHours() )
        print( d.getUTCMilliseconds() )
        print( d.getUTCMinutes() )
        print( d.getUTCMonth() )
        print( d.getUTCSeconds() )
        print( d.getYear() )
        print( d.now() )
        # print( d.onstorage() )
        # print( d.ontimeupdate() )
        print( d.parse( "July 1981" ) )
        print( d.setDate(1) )
        print( d.setFullYear('1982') )
        print( d.setHours(2) )
        # print( d.setItem() )
        print( d.setMilliseconds(12345) )
        print( d.setMinutes(10) )
        print( d.setMonth(10) )
        print( d.setSeconds(10) )
        print( d.setTime() )
        print( d.setUTCDate(1) )
        print( d.setUTCFullYear(1928) )
        print( d.setUTCHours(3) )
        print( d.setUTCMilliseconds(54321) )
        print( d.setUTCMinutes(50) )
        print( d.setUTCMonth(3) )
        print( d.setUTCSeconds(11) )
        print( d.setYear(1987) )
        print( d.toDateString() )
        print( d.toGMTString() )
        print( d.toJSON() )
        print( d.toISOString() )
        print( d.toLocaleDateString() )
        print( d.toLocaleString() )
        print( d.toLocaleTimeString() )
        print( d.toTimeString() )
        print( d.toUTCString() )
        print( d.UTC() )


    # def test_domonic_parse(self):
        # page = domonic.parse("<html><body>'some content'</body></html>")
        # page = domonic.parse("<html><body></body></html>")
        # print(page)

    # def test_domonic_get(self):
    #     print("test_domonic_get-----------=-----------=-----------=-----------=-----------=-----------=-----------=")
    #     page = eval(domonic.get("http://eventual.technology"))
    #     dir(page)


if __name__ == '__main__':
    unittest.main()
