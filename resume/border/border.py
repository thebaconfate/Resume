class Border:
    def __init__(self, width, height, border=25, border_width=None, border_height=None):
        self.__min_width = border_width or border
        self.__min_height = height - (border_height or border)
        self.__max_width = width - (border_width or border)
        self.__max_height = border_height or border
        self.__width = width
        self.__height = height

    @property
    def min_width(self):
        return self.__min_width

    @property
    def min_height(self):
        return self.__min_height

    @property
    def max_width(self):
        return self.__max_width

    @property
    def max_height(self):
        return self.__max_height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
