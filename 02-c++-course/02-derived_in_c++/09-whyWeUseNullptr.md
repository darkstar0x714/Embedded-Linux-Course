# nullptr Vs. NULL;

In C++, `nullptr` is a keyword introduced in C++11 to represent a null pointer. Before C++11, programmers often used the `NULL` macro or `0` to represent null pointers. However, using `nullptr` is generally recommended over `NULL` or `0` for several reasons:

1. **Type Safety:** `nullptr` is a prvalue of type `std::nullptr_t`, which is implicitly convertible and assignable to any pointer type. This makes it type-safe, reducing the risk of errors that can arise from using `NULL` or `0`, which are integer literals.
    ```cpp
    int* ptr = nullptr; // Type-safe
    int* ptr2 = NULL;   // May lead to type-related issues
    ```

2. **Overloading:** The introduction of `nullptr` allows for better overloading of function and operator calls. It helps to distinguish between a null pointer and an integer value.
    ```cpp
    void foo(int);
    void foo(char*);

    foo(nullptr);  // Calls foo(char*)
    foo(NULL);     // May lead to ambiguity
    ```

3. **Template Deduction:** `nullptr` also improves template type deduction in certain cases, where deducing the type from a null pointer might be ambiguous using `0` or `NULL`.
    ```cpp
    template <typename T>
    void bar(T);

    bar(nullptr);  // Deduces T as std::nullptr_t
    bar(NULL);     // Ambiguous type deduction in older code
    ```

4. **Clarity:** Using `nullptr` makes the code more readable by explicitly indicating a null pointer, improving code clarity and making the programmer's intent clearer.
    ```cpp
    if (ptr == nullptr) {
        // Code to handle null pointer
    }

    if (ptr == NULL) {
        // May be less clear, especially for those unfamiliar with older conventions
    ```

