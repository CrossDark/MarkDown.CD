from typing import *
import pickle
from .Core import main, Variable, Syllabus, InlineCode, Extensions

__all__ = [
    'main',  # 主函数
    'indent',  # 添加空格
    'HEAD',  # HTML头部引用
    'Meta',  # 元数据处理器
    'Syllabus',  # 提纲扩展
    'Variable',  # 变量类型提示
    'InlineCode',  # 自定义单行代码
    'Extensions',  # 所有扩展
]
__version__ = '3.4.8'
__author__ = 'CrossDark'
__email__ = 'liuhanbo333@icloud.com'
__source__ = 'https://crossdark.net/'
__license__ = 'MIT'

HEAD = {
    # mathjax
    ('latex',
     'js'): '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>',

    # mermaid
    ('mermaid', 'js'): '<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>',
    ('mermaid', 'init'): '<script>mermaid.initialize({startOnLoad:true})</script>',

    # 代码高亮css
    ('code-highlight', 'css'): '<link rel="stylesheet" href="../Static/styles.css">',

    # Chart.js
    ('chart', 'js'): '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
}


def indent(input_: Union[str, List, Tuple], indent_spaces: int = 4) -> str:
    """
    给字符串中的每一行前面加上缩进。
    :param input_: 原始字符串，可以包含多行。
    :param indent_spaces: 每行前面要添加的空格数，默认为4。
    :return: 带缩进的新字符串。
    """
    # 使用字符串的splitlines()方法分割原始字符串为行列表,如果是可迭代对象则直接遍历
    # 遍历行列表，给每行前面加上相应的缩进，并重新组合成字符串
    return "\n".join(
        f"{' ' * indent_spaces}{line}" for line in (lambda x: x.splitlines() if isinstance(x, str) else x)(input_)
    )


class Meta:
    """
    这是用于处理本模块的元数据的类
    """

    def __init__(self, major: int, minor: int = 0, micro: int = 0, requirements='requirements.txt',
                 long_description='README.md'):
        # 设置版本
        try:
            with open('data.pkl', 'rb') as file:  # 读取上次版本
                latest_version = pickle.load(file)
        except FileNotFoundError:
            pass
        else:
            if latest_version[0] >= major:  # 判断主版本号
                if latest_version[1] >= minor:  # 判断副版本号
                    if latest_version[2] >= micro:  # 判断小版本号
                        raise ValueError('版本不对')
        self.version = f'{major}.{minor}.{micro}'  # 生成版本字符串
        with open('data.pkl', 'wb') as file:  # 记录版本
            pickle.dump((major, minor, micro), file)

        with open(requirements, 'r') as f:  # 设置依赖
            self.requirements = [line.strip() for line in f.readlines()]

        with open(long_description, "r") as fh:
            self.long_description = fh.read()
