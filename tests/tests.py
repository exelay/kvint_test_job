from unittest import TestCase
from unittest.mock import Mock

from core.services import get_or_create_order
from core import services
from core.types import PizzaOrder
from core.settings import DEFAULT_ANSWER
from core.user_interfaces.telegram_bot import get_answer


class TestGetOrCreateOrder(TestCase):

    def test_creating_order(self):
        expected_result = PizzaOrder
        result = get_or_create_order(0)

        self.assertIsInstance(result, expected_result)

    def test_getting_order(self):
        order = PizzaOrder()
        expected_result = order

        services.orders = {0: order}
        result = get_or_create_order(0)

        self.assertEqual(result, expected_result)


class TestGetAnswer(TestCase):

    def test_starting_order(self):
        mocked_message = Mock()
        mocked_message.text = 'хочу пиццу'

        order = PizzaOrder()

        expected_result = 'Какую вы хотите пиццу? Большую или маленькую?'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)

    def test_select_big_pizza(self):
        mocked_message = Mock()
        mocked_message.text = 'большую'

        order = PizzaOrder()
        order.state = 'order_started'

        expected_result = 'Как вы будете платить?'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertEqual(order.pizza_size, 'big')

    def test_select_small_pizza(self):
        mocked_message = Mock()
        mocked_message.text = 'маленькую'

        order = PizzaOrder()
        order.state = 'order_started'

        expected_result = 'Как вы будете платить?'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertEqual(order.pizza_size, 'small')

    def test_select_cash_payment(self):
        mocked_message = Mock()
        mocked_message.text = 'наличкой'

        order = PizzaOrder()
        order.state = 'small_size_selected'
        order.pizza_size = 'small'

        expected_result = 'Вы хотите маленькую пиццу, оплата - наличкой?'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertEqual(order.payment_method, 'cash')

    def test_select_card_payment(self):
        mocked_message = Mock()
        mocked_message.text = 'картой'

        order = PizzaOrder()
        order.state = 'small_size_selected'
        order.pizza_size = 'small'

        expected_result = 'Вы хотите маленькую пиццу, оплата - банковской картой?'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertEqual(order.payment_method, 'card')

    def test_confirm_order(self):
        mocked_message = Mock()
        mocked_message.text = 'да'

        order = PizzaOrder()
        order.state = 'cash_payment_selected'

        expected_result = 'Спасибо за заказ! Если хотите заказать снова, начните с команды /start'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertFalse(order.confirmed)
        self.assertEqual(order.state, 'awaits_order')
        self.assertIsNone(order.payment_method)
        self.assertIsNone(order.pizza_size)

    def test_decline_order(self):
        mocked_message = Mock()
        mocked_message.text = 'нет'

        order = PizzaOrder()
        order.state = 'cash_payment_selected'

        expected_result = 'Жаль что вы отказались( Если всё же захотите заказать, начните с команды /start'
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
        self.assertFalse(order.confirmed)
        self.assertEqual(order.state, 'awaits_order')
        self.assertIsNone(order.payment_method)
        self.assertIsNone(order.pizza_size)

    def test_default_answer(self):
        mocked_message = Mock()
        mocked_message.text = 'f'

        order = PizzaOrder()

        expected_result = DEFAULT_ANSWER
        result = get_answer(mocked_message, order)

        self.assertEqual(result, expected_result)
