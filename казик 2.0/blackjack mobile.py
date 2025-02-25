from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
import random

# Пути к изображениям для карт
card_values = {
    '2': 'cards2.png', '3': 'cards3.png', '4': 'cards4.png',
    '5': 'cards5.png', '6': 'cards6.png', '7': 'cards7.png',
    '8': 'cards8.png', '9': 'cards9.png', '10': 'cards10.png',
    'J': 'cardsj.png', 'Q': 'cardsq.png', 'K': 'cardsk.png',
    'A': 'cardsa.png'
}

card_scores = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class BlackjackApp(App):
    def build(self):
        self.balance_input = 1000
        self.bid_input = 0
        self.dealer_cards = []
        self.user_cards = []

        # Основной макет
        self.layout = FloatLayout()

        # Фон стола
        self.table_background = Image(source='table.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.table_background)

        # Баланс игрока
        self.balance_label = Label(
            text=f"Ваш баланс: {self.balance_input}",
            size_hint=(None, None),
            pos_hint={'x': 0.05, 'y': 0.9},
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.balance_label)

        # Подчеркивание баланса
        self.balance_underline = Image(
            size_hint=(None, None), size=(500, 20),
            pos_hint={'x': -0.055, 'y': 0.91}  # Размер и позиция подчеркивания
        )
        self.layout.add_widget(self.balance_underline)

        # Ввод ставки
        self.bid_textinput = TextInput(
            hint_text="Введите ставку", multiline=False,
            size_hint=(None, None), size=(230, 60),
            pos_hint={'x': 0.004, 'y': 0.8},
            background_normal='bid.png', background_active='bid.png',
            halign='center', font_size=18, padding=(10, 14, 10, 20)
        )
        self.layout.add_widget(self.bid_textinput)

        # Кнопка "Начать игру"
        self.start_button = Button(
            size_hint=(None, None), size=(200, 60),
            pos_hint={'x': 0.013, 'y': 0.7},
            background_normal='start.png',
            background_down='start.png'
        )
        self.start_button.bind(on_press=self.start_game)
        self.layout.add_widget(self.start_button)

        # Кнопка "Взять ещё карту"
        self.another_card_button = Button(
            size_hint=(None, None), size=(200, 60),
            pos_hint={'x': 0.013, 'y': 0.6}, disabled=True,
            background_normal='add.png',
            background_down='add.png'
        )
        self.another_card_button.bind(on_press=self.draw_another_card)
        self.layout.add_widget(self.another_card_button)

        # Кнопка "Хватит"
        self.stay_button = Button(
            size_hint=(None, None), size=(200, 60),
            pos_hint={'x': 0.013, 'y': 0.5}, disabled=True,
            background_normal='stop.png',
            background_down='stop.png'
        )
        self.stay_button.bind(on_press=self.stay)
        self.layout.add_widget(self.stay_button)

        # Сообщение о ходе игры
        self.message_label = Label(
            text="", size_hint=(None, None),
            pos_hint={'x': 0.6, 'y': 0.9},
            font_size=20, color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.message_label)

        # Отображение карт дилера
        self.dealer_layout = BoxLayout(
            orientation='horizontal', spacing=10, size_hint=(None, None),
            pos_hint={'x': 0.3, 'y': 0.6}
        )
        self.layout.add_widget(self.dealer_layout)

        # Отображение карт игрока
        self.user_layout = BoxLayout(
            orientation='horizontal', spacing=10, size_hint=(None, None),
            pos_hint={'x': 0.3, 'y': 0.3}
        )
        self.layout.add_widget(self.user_layout)

        self.update_balance_label()  # Установить начальное подчеркивание
        return self.layout

    def update_balance_label(self):
        self.balance_label.text = f"Ваш баланс: {self.balance_input}"

        # Выбираем цвет подчеркивания в зависимости от баланса
        if self.balance_input >= 200:
            underline_image = 'green.png'  # Зеленая линия, если баланс >= 200
        else:
            underline_image = 'red.png'  # Красная линия, если баланс < 200

        # Обновляем подчеркивание
        self.balance_underline.source = underline_image
        self.balance_underline.reload()  # Перезагружаем изображение

    def start_game(self, instance):
        self.bid_input = int(self.bid_textinput.text) if self.bid_textinput.text.isdigit() else 0
        if self.bid_input > self.balance_input:
            self.message_label.text = "Недостаточно средств для ставки!"
            return
        self.balance_input -= self.bid_input
        self.update_balance_label()  # Обновляем подчеркивание после изменения баланса

        # Очищаем предыдущие карты
        self.dealer_layout.clear_widgets()
        self.user_layout.clear_widgets()

        # Раздаем по две карты дилеру и игроку
        self.dealer_cards = self.draw_card(2)
        self.user_cards = self.draw_card(2)

        # Отображаем карты дилера и игрока с анимацией
        self.update_card_images(self.dealer_layout, self.dealer_cards, hide_first_card=True)
        self.update_card_images(self.user_layout, self.user_cards)

        # Активируем кнопки "Взять ещё карту" и "Хватит"
        self.another_card_button.disabled = False
        self.stay_button.disabled = False
        self.start_button.disabled = True

        self.message_label.text = "Игра началась! Ваш ход."

    def draw_card(self, count):
        return [random.choice(list(card_values.keys())) for _ in range(count)]

    def update_card_images(self, layout, cards, hide_first_card=False):
        layout.clear_widgets()
        for i, card in enumerate(cards):
            card_image = card_values[card] if not (hide_first_card and i == 0) else 'cardsback.jpg'
            img = Image(source=card_image, size_hint=(None, None), size=(0, 0))  # Карта сначала маленькая
            layout.add_widget(img)

            anim = Animation(size=(100, 150), duration=0.3)
            anim.start(img)

    def draw_another_card(self, instance):
        card = self.draw_card(1)[0]
        self.user_cards.append(card)

        img = Image(source=card_values[card], size_hint=(None, None), size=(0, 0))  # Карта сначала маленькая
        self.user_layout.add_widget(img)

        anim = Animation(size=(100, 150), duration=0.3)
        anim.start(img)

        sum_user_cards = self.calculate_score(self.user_cards)

        if sum_user_cards > 21:
            self.message_label.text = "Перебор! Вы проиграли."
            self.reveal_dealer_cards()
            self.end_round()
        elif sum_user_cards == 21:
            self.message_label.text = "Вы набрали 21! Ваш ход завершен."
            self.stay(instance)

    def calculate_score(self, cards):
        return sum(card_scores[card] for card in cards)

    def reveal_dealer_cards(self):
        self.update_card_images(self.dealer_layout, self.dealer_cards, hide_first_card=False)

    def stay(self, instance):
        sum_user_cards = self.calculate_score(self.user_cards)
        sum_dealer_cards = self.calculate_score(self.dealer_cards)

        self.reveal_dealer_cards()

        while sum_dealer_cards < 17:
            card = self.draw_card(1)[0]
            self.dealer_cards.append(card)
            self.update_card_images(self.dealer_layout, self.dealer_cards)
            sum_dealer_cards = self.calculate_score(self.dealer_cards)

        if sum_dealer_cards > 21 or sum_user_cards > sum_dealer_cards:
            self.message_label.text = "Вы выиграли!"
            self.balance_input += self.bid_input * 2
        elif sum_user_cards < sum_dealer_cards:
            self.message_label.text = "Дилер выиграл!"
        else:
            self.message_label.text = "Ничья!"

        self.end_round()

    def end_round(self):
        self.another_card_button.disabled = True
        self.stay_button.disabled = True
        self.start_button.disabled = False
        self.bid_textinput.text = ""
        self.update_balance_label()

if __name__ == '__main__':
    BlackjackApp().run()
