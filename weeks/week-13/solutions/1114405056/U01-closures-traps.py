"""U01: common closure and default-argument traps."""


def add_to_cart(item, cart=[]):  # noqa: B006 - intentional demo of bad pattern
    cart.append(item)
    return cart


def add_to_cart_safe(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def make_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_visit_tracker():
    visited = set()

    def visit(node):
        if node in visited:
            return False
        visited.add(node)
        return True

    return visit


if __name__ == "__main__":
    print("=== mutable default trap ===")
    print(add_to_cart("apple"))
    print(add_to_cart("banana"))
    print(add_to_cart("grape"))

    print("\n=== safe default pattern ===")
    print(add_to_cart_safe("apple"))
    print(add_to_cart_safe("banana"))

    print("\n=== late binding trap ===")
    funcs = []
    for i in range(5):
        funcs.append(lambda: i)
    print([f() for f in funcs])

    print("\n=== fix late binding ===")
    funcs_ok = []
    for i in range(5):
        funcs_ok.append(lambda i=i: i)
    print([f() for f in funcs_ok])

    print("\n=== nonlocal counter ===")
    c1 = make_counter()
    c2 = make_counter(10)
    print(c1(), c1(), c1())
    print(c2(), c2())
    print(c1())

    print("\n=== closure with local state ===")
    visit = make_visit_tracker()
    print([visit(n) for n in [1, 2, 1, 3, 2, 4]])
