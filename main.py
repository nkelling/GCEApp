from gceapp import GceApp
import time
import urllib2
import sys


def main():
    while 1 != 0:
        ### Declare GceApp objects here
        # <Account Name> = GceApp(<Project Name, <Key File>)
        # testaccount = GceApp('totemic-blitz-177823', 'my_first_project-test.json')

        try:
            # testaccount.list_instances()
            # testaccount.start_instances()

        except urllib2.HTTPError as error:
            print error
        except Exception as catchAll:
            print catchAll

        time.sleep(600)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
