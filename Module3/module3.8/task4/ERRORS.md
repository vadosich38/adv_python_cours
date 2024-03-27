Исправленные ошибки
========
Тестирование
----------
***При тестировании методов класса были выявлены ошибки. Вывод результатов запуска тестирования:***
    
    test_age_is_correct (tests.test_person_class.TestPerson.test_age_is_correct) ... FAIL
    ____________________________________________________________________________________
    test_change_name (tests.test_person_class.TestPerson.test_change_name) ... FAIL
    ____________________________________________________________________________________
    test_change_address (tests.test_person_class.TestPerson.test_change_address) ... FAIL
    ____________________________________________________________________________________
    test_is_homeless (tests.test_person_class.TestPerson.test_is_homeless) ... ERROR

Ошибка при тестировании test_age_is_correct
-----------------------------------------
**Рассмотрим код метода:**

    def get_age(self):
        now = datetime.now()
        return self.yob - now.year
Оказывается метод возвращает результат вычисления разницы года рождения от текущего года, что, естветственно, является 
отрицательным значением.

***Исправленный код будет выглядеть так:***
    
    def get_age(self):
        now = datetime.now()
        return now.year - self.yob

Ошибка при тестировании test_change_name
-----------------------------------------
**Давайте рассмотрим код метода, меняющего имя**
    
    def set_name(self, name):
        self.name = self.name
Код не использует переданный элемент, а лишь перезаписывает существующее значение из self.name

***Исправленный код будет выглядеть так:***
    
    def set_name(self, name):
        self.name = name

Ошибка при тестировании test_change_address
-----------------------------------------
**Рассмотрим код метода**

    def set_address(self, address):
        self.address == address
В данном коде используется оператор сравнения "==" вместо оператора присваивания "=".

***Исправленный код будет выглядеть так:***
        
    def set_address(self, address):
        self.address = address

Ошибка при тестировании test_is_homeless
-----------------------------------------
**Рассмотрим код метода**

    def is_homeless(self):
        """
        returns True if address is not set, false in other case
        """
        return address is None
Метод должен возвращать bool значение. Если адрес не заполнен, вернется True, в других случаях вернется False.
Проверка выглядит корректно, но такого аргумента, как address в метоже не существует, из-за этого и возникает ошибка.
        
    return address is None
           ^^^^^^^
    NameError: name 'address' is not defined. Did you mean: 'self.address'?

***Исправленный код будет выглядеть так:***
        
    def is_homeless(self):
        """
        returns True if address is not set, false in other case
        """
        return self.address is None

Теперь все работает корректно и результаты тестирвоания методов удовлетворяют наши условия.
===================================

    vladyslav@MacBook-Air-Vladyslav task4 % python3 -m unittest -v
    test_address_is_correct (tests.test_person_class.TestPerson.test_address_is_correct) ... ok
    test_age_is_correct (tests.test_person_class.TestPerson.test_age_is_correct) ... ok
    test_change_address (tests.test_person_class.TestPerson.test_change_address) ... ok
    test_change_name (tests.test_person_class.TestPerson.test_change_name) ... ok
    test_get_name_is_correct (tests.test_person_class.TestPerson.test_get_name_is_correct) ... ok
    test_is_homeless (tests.test_person_class.TestPerson.test_is_homeless) ... ok
    
    ----------------------------------------------------------------------
    Ran 6 tests in 0.000s
    
    OK

