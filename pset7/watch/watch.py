import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r'src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s):
        return f"https://youtu.be/{url.group(2)}"
    else:
        return None
    # match = re.search(f'.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    # if match:
    #     link = "https://yout.be/" + match.group(1)
    #     return link
    # else:
    #     return False

    # if re.search(r"<iframe(.)*><\/iframe>", s):
    #     url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-z0-9]+)", s)
    #     if url:
    #         split_url = url.groups()
    #         return "https://yout.be/" + split_url[3]
    #     else:
    #         return False

if __name__ == "__main__":
    main()