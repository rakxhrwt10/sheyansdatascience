li = [x for x in range(0,5)]

print(li)

for l in li:
    try:
        if l // 2== 0:   # yeh hamesha error dega
            print("hello")
    except Exception as err:
        print(f"zero division error{err}")

    else:
        print("there was no erro")

    finally:
        print("i will excute no matter what")


        


    