import logging

from fixtures.pages.searsh import SearchProduct

shop_logger = logging.getLogger('ProductShop')


class TestSearch:
    def test_search_existing_product(self, shop_application):
        """
        Steps:
        1. Open page
        2. Input product name
        3. Click searh_button
        4. Check result
        """
        shop_logger.info('START')

        shop_application.open_page()

        shop_logger.info('Open page with search input')
        # TODO Реализовать словарик со всеми названиями продуктов
        SearchProduct().search_product(self, product_name='tomate')
        shop_logger.info(f'Filling registration info: login {registration_data.log}, password {registration_data.passw}, name{registration_data.name}, surname {registration_data.surname} ')
        assert 1 == 1

    def test_search_non_existent_product(self, shop_application):
        """
        Steps:
        1. Open page
        2. Input product name non-existent in data base
        3. Click searh_button
        4. Check result
        """
        shop_logger.info('START')

        shop_application.open_page()

        shop_logger.info('Open page with search input')

        assert 1 == 1
