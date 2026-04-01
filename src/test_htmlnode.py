import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(props)
        self.assertIsNotNone(node)
        self.assertTrue(node) == '"href": "https://www.google.com", "target": "_blank"'

        props = ""
        node = HTMLNode(props)
        self.assertIsNotNone(node)
        self.assertTrue(node) == ""

        props = "Hello, world"
        node = HTMLNode(props)
        self.assertIsNotNone(node)
        self.assertTrue(node) == ValueError


    def test_repr(self):
        tag = "<a>"
        value = "Hello, world"
        children = "1"
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(tag, value, children, props)
        self.assertTrue(node) == 'HTMLNode(<a>, Hello, world, 1, href: "https://www.google.com", target: "_blank")'

if __name__ == "__main__":
    unittest.main()
