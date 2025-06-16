from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Punctuation, Literal



class PycharmStyle(Style):
    """
    Estilo inspirado no esquema de cores do PyCharm para uso com Pygments.
    """
    styles = {
        Comment.Single:       '#797D7D',  # comentário
        Comment.Multilin:     '#5F826B',  # """ comentário """
        Keyword:              '#CF8E6D',
        Name:                 '#BCBEC4',
        Punctuation:          '#BCBEC4',  # {}[](),:
        Name.Exception:       '#8888C6',
        Name.Variable.Magic:  '#B000B2',  # __slots__, __name__
        # Name.Variable.Magic:  '#BCBEC4',  # __slots__, __name__
        Name.Namespace:       '#BCBEC4',
        Name.Function:        '#56A8F5',
        Name.Function.Magic:  '#B000B2',
        Name.Builtin:         '#8888C6',
        Name.Builtin.Pseudo:  '#94558D',  # 'self'
        Keyword.Reserved:     '#CF8E6D',
        Name.Argument:        '#AA4926',       # func call named args -> func(named_arg=10) Nota: O lexer padrão (PythonLexer) não gera esse token, foi necessário modificar lexer para CustompythonLexer que deve ser registrado executando install.py e acessado através de \begin{minted}{custompython}...
        Operator.Word:        '#CF8E6D',  # 'in', 'or', 'and'
        String:               '#6AAB73',
        String.Affix:         '#6AAB73',  # f', r'
        String.Interpol:      'bold #CF8E6D',  # {} e : em f'strings
        String.Escape:        'bold #CF8E6D',  # \n em f'strings
        Name.Decorator:       '#B3AE60',
        Name.Class:           'bold #BCBEC4',
        Number:               '#2AABB8',
        Operator:             '#BCBEC4',
        Generic:              '#BCBEC4',
        Error:                'border:#FF0000'
    }
    default_style = ""
