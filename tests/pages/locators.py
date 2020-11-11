class MainPL():
    MAIN_PAGE_URL = 'https://demo-games.infomatika.ru/ru/'
    BTN_EVENTS_BUY = '.events__buy'
    BTN_ABONEMENT_BUY = '.subscription'
    BTN_SPLIT_BUY = '.split'
    USER_PROFILE_DROPDOWN = '#dropdown__btn--1'



class AbonementPL():
    ABONEMENT_PAGE_URL = 'https://demo-games.infomatika.ru/ru/subscription/list'
    SUBSCRIPTION_COUNT = '#js-subscription-count'
    SUBSCRIPTION_COUNT_BTN_NEXT = '/subscription/pre-index/21'
    BTN_SUBSCRIPTION_CHOOSE = '.js-subscription-choose'
    BTN_SUBSCRIPTION_PLUS = '.subscription__plus'
    BTN_SUBSCRIPTION_MINUS = '.subscription__minus'
    SUBSCRIPTION_COUNT_BTN_CONTINUE = '#js-subscription-continue'
    BTN_SUBSCRIPTION_NEXT = '.btn_usual'
    TEXT_COUNT_SUBSCRIPTION = '#js-subscription-count > strong'
    CHECK_BOX_ALL = '#js-checkbox-all'
    BTN_SUBSCRIPTION_BUY = '#js-subscription-buy'

class SectorPL():
    SVG_SECTOR = '#svg > g[price]'
    SVG_EMPTY_SECTOR = '#svg > g[price]'
    SVG_PLACES = '#svg > g.active'
    SVG_EMPTY_PLACE = '#svg > g.active'
    TICKETS_CONTENT_BAR = '.tickets__content'
    BTN_BASKET = '/ru/orders/cart'
    BTN_NEXT_MODAL_WINDOWS = '.js-hover-out'
    BTN_ZOOM_MINUS = '#js-plan-zoom-out'
    BTN_ZOOM_PLUS = '#js-plan-zoom-in'
    BTN_SPLIT_BUY = '.bottom__word_buy'
    SVG_PLAN = '#svg'
    SVG_SPLIT_FIRST_PLAN_EMPTY_SECTOR = '.places__twice-content[data-selenium="first-plan"] #svg > g[price]'
    SVG_SPLIT_SECOND_PLAN_EMPTY_SECTOR = '.places__twice-content[data-selenium="second-plan"] #svg > g[price]:not(.inactive)'


class HeaderPL():
    NUMBER_ITEMS_BASKET = '.header__link-count'
    BTN_LOGIN = '.header__btn_login'
    FORM_LOGIN_EMAIL = '#login-form-login'
    FORM_LOGIN_PASSWORD = '#login-form-password'
    BTN_FORM_LOGIN = '.auth_btn'
    MENU_ABONEMENT = '/ru/subscription/list'
    BTN_GAMBURGER = '#js-hamburger'
    ICON_LOGIN = '.header__link-text_login'
    BTN_PRIORITY_PLACES = '/ru/verification'

class BasketPL():
    BTN_ALL_CLEAR =  '#js-order-clear'
    TEXT_CLEAR_BASKET = 'div.lk__small-title'
    BTN_TICKETS_EVENT_DELETE = '.order__delete-text'
    ELEMENT_PAGE_LOAD = '.ready-for-test'
class PriorityPL():
    BTN_SELECT_PRIORITY_PLACES = '/ru/verification/seats'
    CHECKBOX_ALL = '.purchase__top .checkbox__block'
    CHECKBOX_PLACES_ONE = '#verification-seats-form tr:nth-child(1) .checkbox'
    CHECKBOX_PLACES_TWO = '#verification-seats-form tr:nth-child(2) .checkbox'
    BTN_BUY_PRIORITY = '.purchase__bottom .btn'
