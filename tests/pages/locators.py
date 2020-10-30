class MainPL():
    MAIN_PAGE_URL = 'https://demo-games.infomatika.ru/ru/'
    BTN_EVENTS_BUY = '.single'
    BTN_ABONEMENT_BUY = '.subscription'
    BTN_SPLIT_BUY = '.split'
    USER_PROFILE_DROPDOWN = '#dropdown__btn--1'



class AbonementPL():
    ABONEMENT_PAGE_URL = 'https://demo-games.infomatika.ru/ru/subscription/list'
    SUBSCRIPTION_COUNT = '#js-subscription-count'
    SUBSCRIPTION_COUNT_BTN_NEXT = '/subscription/pre-index/21'
    BTN_SUBSCRIPTION_CHOOSE = '.subscription__choose'
    BTN_SUBSCRIPTION_PLUS = '.subscription__plus'
    BTN_SUBSCRIPTION_MINUS = '.subscription__minus'
    SUBSCRIPTION_COUNT_BTN_CONTINUE = '#js-subscription-continue'
    BTN_SUBSCRIPTION_NEXT = '.btn_usual'


class SectorPL():
    SVG_SECTOR = '#svg > g[price]'
    SVG_EMPTY_SECTOR = '#svg > g[price]'
    SVG_PLACES = '#svg > g.active'
    SVG_EMPTY_PLACE = '#svg > g.active'
    TICKETS_CONTENT_BAR = '.tickets__content'
    BTN_BASKET = '/ru/orders/cart'


class HeaderPL():
    NUMBER_ITEMS_BASKET = '.header__link-count'
    BTN_LOGIN = '.header__btn_login'
    FORM_LOGIN_EMAIL = '#login-form-login'
    FORM_LOGIN_PASSWORD = '#login-form-password'
    BTN_FORM_LOGIN = '.auth_btn'
    MENU_ABONEMENT = '/ru/subscription/list'
    BTN_GAMBURGER = '#js-hamburger'
    ICON_LOGIN = '.header__link-text_login'

class BasketPL():
    BTN_ALL_CLEAR =  '#js-order-clear'
    TEXT_CLEAR_BASKET = 'div.lk__small-title'
    BTN_TICKETS_EVENT_DELETE = '.order__delete-text'
    ELEMENT_PAGE_LOAD = '.ready-for-test'
