from solution import Uber, XL, Van, Car
import pytest


def test_Create_Uber():
    trip1 = Uber(10, True)
    trip2 = Uber(1, False)

    assert trip1.distance == 10
    assert trip1.is_hot == True

    assert trip2.distance == 1
    assert trip2.is_hot == False


def test_fare_is_hot():
    trip1 = Uber(10, True)

    cost = trip1.fare(5, 2)

    assert cost == 50


def test_fare_not_hot():
    trip2 = Uber(1, False)

    cost = trip2.fare(5, 2)

    assert cost == 2.5


def test_Create_XL():
    assert issubclass(XL, Uber)
    assert XL.capacity_check is Uber.capacity_check
    assert XL.fare is Uber.fare

    trip1 = XL(10, True)

    assert trip1.capacity == 6


def test_Create_Van():
    assert issubclass(Van, Uber)
    assert Van.capacity_check is Uber.capacity_check
    assert Van.fare is Uber.fare

    trip1 = Van(10, True)

    assert trip1.capacity == 8


def test_Create_Car():
    assert issubclass(Car, Uber)
    assert Car.capacity_check is Uber.capacity_check
    assert Car.fare is Uber.fare

    trip1 = Car(10, True)

    assert trip1.capacity == 4


def test_Capacity_Check_XL_fail():
    trip1 = Uber(10, True)

    with pytest.raises(ValueError):
        trip1.capacity_check(6, 7)


def test_Capacity_Check_Van_fail():
    trip1 = Uber(10, True)

    with pytest.raises(ValueError):
        trip1.capacity_check(8, 9)


def test_Capacity_Check_Car_fail():
    trip1 = Uber(10, True)

    with pytest.raises(ValueError):
        trip1.capacity_check(4, 5)
