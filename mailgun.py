
import requests
from bs4 import BeautifulSoup
import argparse


def send_html_message(domain, sender, to, cc, bcc, subject, body, attach_files, html ):
    template = None
    files=[]
    
    if html is not None:
        with open(html) as f:
            soup = BeautifulSoup(f, "html.parser")
            template = soup.prettify()
    if attach_files:
        for i in attach_files:
            files.append(("attachment", (i, open(i,"rb").read())))

    return requests.post(
        "https://api.mailgun.net/v3/"+domain+"/messages",
        auth=("api", "  yourKeys"),
        files=files,
        data={"from": sender,
              "to": to, 
              "cc": cc,
              "bcc": bcc,             
              "subject": subject,
              "text": body,
              "html": template,}
              )         
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Relay mail from Mailgun',
                                     epilog="Example: python3 mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'")

    parser.add_argument('-d', '--domain', help='-d example.com', type=str)
    parser.add_argument('-f', '--sender', help='-f address', type=str)
    parser.add_argument('-t', '--to', help='-t address', type=str, nargs="+")
    parser.add_argument('-cc', '--cc', help='-cc address', type=str, nargs="+")
    parser.add_argument('-bcc', '--bcc', help='-bcc address', type=str, nargs="+")
    parser.add_argument('-s', '--subject', help='"text subject"', type=str)
    parser.add_argument('-m', '--body', help='"text msg"', type=str)
    parser.add_argument('-a', '--attach', help='filename', nargs="+")
    parser.add_argument('-o', '--html', help='html content', type=str, default=None)
    args = parser.parse_args()
    
    response = send_html_message(args.domain, args.sender, args.to, args.cc, args.bcc, args.subject, args.body, args.attach, args.html)
    print (response.text )
