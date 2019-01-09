import base64
import argparse
import win32clipboard as w
import win32con

def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description='Transfor image to base64')
    parser.add_argument('-a', '--address', type=str, help='image address')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    bs64code = transfor(addr=args["address"]) 
    _print(bs64code)
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, bs64code)
    w.CloseClipboard()


def transfor(addr):
    f=open(addr,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    return ls_f

def _print(bs64code):
    """ 在终端界面输出结果
    :param bs64code: 转换后的结果
    """
    if not bs64code:
        return
    print(bs64code)

if __name__ == "__main__":
    command_line_runner()
