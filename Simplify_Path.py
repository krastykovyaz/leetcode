class Solution:
    def SimplePath(self, path: str)-> str:
        path_list = path.split('/')
        new_path = []
        for word in path_list:
            if new_path and word == "..":
                new_path.pop()
            if word != '.' and word != '..':
                new_path.append(word)
        str_path = '/'.join(new_path).rstrip('/')

        return str_path if str_path else '/'




if __name__=='__main__':
    s = Solution()
    path ="/a/./b/../../c/"
    print(s.SimplePath(path))