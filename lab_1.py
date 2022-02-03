class Sorter():
    dict = {}

    def sort(s:str):
        max_len = 0

        for i in range(len(s)):
            curr = set()
            curr_dict = {}
            index = i

            for j in s[i:]:
                if j in curr:
                    break
                curr.add(j)
                curr_dict[index] = j
                index += 1

            curr_len = len(curr)
            if curr_len > max_len:
                max_len = curr_len
                dict = curr_dict

        print(max_len)
        print(dict)

if __name__ == '__main__':
    sorter = Sorter
    sorter.sort('aaabcbb')
    sorter.sort('abcabcbb')
    sorter.sort('pwwkew')
    sorter.sort('abcd mad3efil kekw')
    sorter.sort('abcd ma3efil kekw')