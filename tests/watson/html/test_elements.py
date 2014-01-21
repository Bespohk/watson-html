# -*- coding: utf-8 -*-
from pytest import raises
from watson.html.elements import flatten_attributes, TagMixin


class TestFlattenAttributes(object):

    def test_flatten(self):
        attrs = {'class': 'menu', 'id': 'MainMenu'}
        assert flatten_attributes(attrs) == 'class="menu" id="MainMenu"'

    def test_flatten_forget_empty(self):
        attrs = {'class': 'menu', 'id': None}
        assert flatten_attributes(attrs) == 'class="menu"'

    def test_flatten_keep_empty(self):
        attrs = {'class': 'menu', 'id': None}
        assert flatten_attributes(attrs, True) == 'class="menu" id=""'


class TestTagMixin(object):

    def test_initialize(self):
        mixin = TagMixin(id='Test')
        assert 'id' in mixin.attributes

    def test_render(self):
        with raises(NotImplementedError):
            str(TagMixin(id='Test'))
