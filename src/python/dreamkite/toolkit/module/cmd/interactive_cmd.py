from cmd import Cmd

'''
我们需要知道输入行包括两个部分：命令和参数
'''


class Cli(Cmd):
    u"""help
     这是doc
    """
    prompt = 'dreamKiteCmd>'
    intro = 'Welcome to the DreamKite shell.   Type help or ? to list commands.\n'
    file = None

    def __init(self):
        Cmd.__init__(self)

    def do_record(self, arg):
        '用于记录操作日志，Save future commands to filename:  RECORD dkShell.log'
        self.file = open(arg, 'w')

    def do_hello(self, line):
        print("hello", parse(line))
        # 返回True则会跳出循环，否则接着循环
        return True

    def precmd(self, line):
        print("print this line before do a command")
        line = line.lower()
        if self.file:
            print(line, file=self.file)
        return Cmd.precmd(self, line)

    def preloop(self):
        print("print this line before entering the loop")

    def postloop(self):
        # print 'Bye!'
        print("print this line after leaving the loop")

    def precmd(self, line):
        print("print this line before do a command")
        return Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        print("print this line after do a command")
        return Cmd.postcmd(self, stop, line)

    def do_exit(self, arg):
        print("Bye.")
        if self.file:
            self.file.close()
            self.file = None
        return True

    # 当输入空行的时候，我们可以重载emptyline()来处理：

    def emptyline(self):
        print('please input command!')

    # 当输入无法识别的命令时，使用default(line)来处理

    def default(self, line):
        print('please input correct command!')


def parse(arg):
    return tuple(arg.split())


if __name__ == '__main__':
    # 按下ctrl+c之后能够正常退出不报错
    try:
        cli = Cli()
        cli.cmdloop()
        # 输入hello jun kai
    except:
        exit()
