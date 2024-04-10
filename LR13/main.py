
def task1() -> None:
    add_ten = lambda x: x + 10

    print(f"4 + 10 = {add_ten(4)}")
    return


def task2() -> None:
    add_three = lambda a, b, c: a + b + c

    print(f"4 + 5 + 12 = {add_three(4, 5, 12)}")
    return


def task3() -> None:
    a = lambda: 2
    b = lambda x: 1
    c = lambda x: x
    d = lambda x, y: x + y
    e = lambda x, y: max(x, y)
    f = lambda x, y: f"{y}{x}"
    g = lambda x: lambda y: f"{x}{y}"
    h = lambda: lambda x: 5 + x
    i = lambda x, y: lambda z: x + z
    j = lambda x: x
    k = lambda x: x + 1
    m = lambda x: x + 3
    n = lambda: 2
    o = lambda x: x
    p = lambda x, y: lambda z: x(z) + y(0)
    q = lambda x: lambda y: f"{y()} {x}"
    r = lambda x, y: lambda z: int(z() + x / y())
    s = lambda x: x(lambda: lambda y: y)

    def t(x):
        return lambda y: f"{x}{y}"

    def u(z):  # use t!
        return f"{t('arc')('cos')}{z}"

    def v():
        return u("ecant")

    print(a())
    print(b(3))
    print(b(10))
    print(b(2))
    print(c(1))
    print(c(3))
    print(d(1, 3))
    print(d(2, 5))
    print(e(1, 3))
    print(e(2, 5))
    print(f(2, 5))
    print(f(3, 1))
    print(g(1)(2))
    print(g(2)(1))
    print(h()(2))
    print(h()(3))
    print(i(2, 5)(2))
    print(i(3, 5)(2))
    print(j(lambda x: 2)(1))
    print(j(lambda x: x + 1)(1))
    print((lambda x: x(2))(k))
    print((lambda x: lambda y: x(y()))(m)(n))
    print(o("cal"))
    print(p(lambda x: x + 2, lambda x: x + 3)(1))
    print(q("veggies")(lambda: "eat"))

    happy = r(30, lambda: new_year() // 1000)
    new_year = (lambda x: lambda: x)(2000)
    print(happy(new_year))

    print(s(lambda x: x()('cal')))
    print(t("ta")("n"))
    print(u("sine"))
    print(v())
    return


def task4() -> None:
    a = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
    get_pows = lambda x: [y*y for y in x]

    print(get_pows(a))


def task5() -> None:
    a = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
    get_product = lambda l: 1 if len(l) == 0 else (lambda x: x[0] * get_product(x[1:]))(l)

    print(get_product(a))


def task6() -> None:
    lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
           (1805832, "West Virginia"), (39865590, "California")]

    sorted_lst = sorted(lst, key=lambda x: x[1][-1], reverse=True)
    print(sorted_lst)


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    return


if __name__ == "__main__":
    main()