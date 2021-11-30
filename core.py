from transitions import Machine


class PizzaOrder:
    states = [
        {'name': 'awaits_order', 'on_enter': ['ask_about_order', 'cleanse_order']},
        {'name': 'order_started', 'on_enter': 'ask_pizza_size'},
        {'name': 'big_size_selected', 'on_enter': ['select_pizza_size', 'ask_payment_method']},
        {'name': 'small_size_selected', 'on_enter': ['select_pizza_size', 'ask_payment_method']},
        {'name': 'cash_payment_selected', 'on_enter': ['select_payment_method', 'ask_about_order_confirmation']},
        {'name': 'card_payment_selected', 'on_enter': ['select_payment_method', 'ask_about_order_confirmation']},
        {'name': 'order_confirmed', 'on_enter': 'acknowledge_order'},
        {'name': 'order_declined', 'on_enter': 'reject_order'},
    ]
    transitions = [
        {'trigger': 'start_order', 'source': 'awaits_order', 'dest': 'order_started'},
        {'trigger': 'select_big_pizza', 'source': 'order_started', 'dest': 'big_size_selected'},
        {'trigger': 'select_small_pizza', 'source': 'order_started', 'dest': 'small_size_selected'},
        {'trigger': 'select_cash_payment', 'source': ['big_size_selected', 'small_size_selected'],
         'dest': 'cash_payment_selected'},
        {'trigger': 'select_card_payment', 'source': ['big_size_selected', 'small_size_selected'],
         'dest': 'card_payment_selected'},
        {'trigger': 'confirm_order', 'source': ['cash_payment_selected', 'card_payment_selected'],
         'dest': 'order_confirmed'},
        {'trigger': 'decline_order', 'source': ['cash_payment_selected', 'card_payment_selected'],
         'dest': 'order_declined'},
        {'trigger': 'clean_order', 'source': ['decline_order', 'confirm_order'], 'dest': 'awaits_order'},
    ]
    starting_message = 'Привет, у меня ты можешь заказать пиццу. Просто напиши: "Хочу пиццу" 😉'
    message = None

    payment_method = None
    pizza_size = None
    confirmed = False

    def __init__(self):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='awaits_order')
        self.message = self.starting_message

    def ask_pizza_size(self):
        self.message = 'Какую вы хотите пиццу? Большую или маленькую?'

    def select_pizza_size(self):
        if self.state == 'big_size_selected':
            self.pizza_size = 'big'
        elif self.state == 'small_size_selected':
            self.pizza_size = 'small'

    def ask_payment_method(self):
        self.message = 'Как вы будете платить?'

    def select_payment_method(self):
        if self.state == 'cash_payment_method':
            self.payment_method = 'cash'
        elif self.state == 'card_payment_selected':
            self.payment_method = 'card'

    def ask_about_order_confirmation(self):
        self.message = f'Вы хотите {self.pizza_size} пиццу, оплата - {self.payment_method}?'

    def acknowledge_order(self):
        self.message = 'Спасибо за заказ! Если хотите заказать снова, начните с команды /start'
        self.confirmed = True

    def reject_order(self):
        self.message = 'Жаль что вы отказались( Если всё же захотите заказать, начните с команды /start'

    def cleanse_order(self):
        self.payment_method = None
        self.pizza_size = None
        self.confirmed = False

    def ask_about_order(self):
        self.message = self.starting_message
