class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        dis = 1 - discount / 100
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if len(word) >=2 and word[0] == "$":
                oldPrice = word[1:]
                if oldPrice.isdigit():
                    price = int(oldPrice)*dis
                    words[i] = "${:.2f}".format(price)
        return " ".join(words)

if __name__ == "__main__":
    print(Solution().discountPrices("there are $1 $2 and 5$ candies in the shop",50))
    print(Solution().discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))