import unittest

from src import Serializer as ser
from tests.test_objects import *


class SerializerTester(unittest.TestCase):

    def __init__(self, method):
        super().__init__(method)
        self.json_serializer = ser.Serializer()
        self.json_serializer.path = json_file
        self.json_serializer.extension = 'json'
        self.pickle_serializer = ser.Serializer(path=pickle_file, extension='pickle')
        self.yaml_serializer = ser.Serializer(path=yaml_file, extension='yaml')

    def test_str(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(str1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(str1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(str1))
        self.assertEqual(json_obj, str1)
        self.assertEqual(pickle_obj, str1)
        self.assertEqual(yaml_obj, str1)

    def test_int(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(num1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(num1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(num1))
        self.assertEqual(json_obj, num1)
        self.assertEqual(pickle_obj, num1)
        self.assertEqual(yaml_obj, num1)

    def test_float(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(flot1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(flot1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(flot1))
        self.assertEqual(json_obj, flot1)
        self.assertEqual(pickle_obj, flot1)
        self.assertEqual(yaml_obj, flot1)

    def test_bool(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(bool1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(bool1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(bool1))
        self.assertEqual(json_obj, bool1)
        self.assertEqual(pickle_obj, bool1)
        self.assertEqual(yaml_obj, bool1)

    def test_bytes(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(bytes1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(bytes1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(bytes1))
        self.assertEqual(json_obj, bytes1)
        self.assertEqual(pickle_obj, bytes1)
        self.assertEqual(yaml_obj, bytes1)

    def test_bytearray(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(bytearr1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(bytearr1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(bytearr1))
        self.assertEqual(json_obj, bytearr1)
        self.assertEqual(pickle_obj, bytearr1)
        self.assertEqual(yaml_obj, bytearr1)

    def test_builtin(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(bltfunc))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(bltfunc))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(bltfunc))
        self.assertEqual(json_obj(lst1), bltfunc(lst1))
        self.assertEqual(pickle_obj(lst1), bltfunc(lst1))
        self.assertEqual(yaml_obj(lst1), bltfunc(lst1))

    def test_set(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(set1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(set1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(set1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))
        self.assertEqual(json_obj, set1)
        self.assertEqual(pickle_obj, set1)
        self.assertEqual(yaml_obj, set1)
        # self.assertEqual(toml_obj, lst1)

    def test_frozenset(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(frzset1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(frzset1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(frzset1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))
        self.assertEqual(json_obj, frzset1)
        self.assertEqual(pickle_obj, frzset1)
        self.assertEqual(yaml_obj, frzset1)
        # self.assertEqual(toml_obj, lst1)

    def test_tuple(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(tpl1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(tpl1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(tpl1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))
        self.assertEqual(json_obj, tpl1)
        self.assertEqual(pickle_obj, tpl1)
        self.assertEqual(yaml_obj, tpl1)
        # self.assertEqual(toml_obj, lst1)

    def test_list(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(lst1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(lst1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(lst1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))
        self.assertEqual(json_obj, lst1)
        self.assertEqual(pickle_obj, lst1)
        self.assertEqual(yaml_obj, lst1)
        # self.assertEqual(toml_obj, lst1)

    def test_simple_dicts(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(dict1))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(dict1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(dict1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(dict1))
        self.assertEqual(json_obj, dict1)
        self.assertEqual(pickle_obj, dict1)
        self.assertEqual(yaml_obj, dict1)
        # self.assertEqual(toml_obj, dict1)
