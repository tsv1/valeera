import unittest
import district42.json_schema as schema
from validator_testcase import ValidatorTestCase


class TestArrayOfValidator(ValidatorTestCase):
  
  def test_it_validates_type(self):
    self.assertValidationFails(None,  schema.array_of(schema.integer))
    self.assertValidationFails(False, schema.array_of(schema.integer))
    self.assertValidationFails(0,     schema.array_of(schema.integer))
    self.assertValidationFails('[]',  schema.array_of(schema.integer))
    self.assertValidationFails({},    schema.array_of(schema.integer))

  def test_it_validates_items_schema(self):
    self.assertValidationPasses(['banana', 'cucumber'], schema.array_of(schema.string))
    self.assertValidationPasses([1, 2, 3],              schema.array_of(schema.integer))
    self.assertValidationPasses([None],                 schema.array_of(schema.null))

    self.assertValidationFails(['banana', 'cucumber'], schema.array_of(schema.integer))
    self.assertValidationFails([1, 2, 3],              schema.array_of(schema.string))

  def test_it_validates_length(self):
    self.assertValidationPasses(['banana'], schema.array_of(schema.string).length(1))
    self.assertValidationPasses([0],        schema.array_of(schema.integer).length(1, 2))
    self.assertValidationPasses([0, 1],     schema.array_of(schema.integer).length(1, 2))
    self.assertValidationPasses(['banana'], schema.array_of(schema.string).min_length(1))
    self.assertValidationPasses(['banana'], schema.array_of(schema.string).max_length(1))

    self.assertValidationFails([1],       schema.array_of(schema.integer).length(2))
    self.assertValidationFails([1, 2, 3], schema.array_of(schema.integer).length(2))
    self.assertValidationFails([0, 1],    schema.array_of(schema.integer).length(0, 1))
    self.assertValidationFails([0, 1],    schema.array_of(schema.integer).length(3, 5))
    self.assertValidationFails([],        schema.array_of(schema.integer).min_length(1))
    self.assertValidationFails([0, 1],    schema.array_of(schema.integer).max_length(1))

  def test_it_validates_nullable(self):
    self.assertValidationPasses(None, schema.array_of(schema.object).nullable)

    self.assertValidationFails(False, schema.array_of(schema.object).nullable)
    self.assertValidationFails(0,     schema.array_of(schema.object).nullable)
    self.assertValidationFails('[]',  schema.array_of(schema.object).nullable)
    self.assertValidationFails({},    schema.array_of(schema.object).nullable)

if __name__ == '__main__':
  unittest.main()
