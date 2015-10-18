import unittest
import district42.json_schema as schema
from validator_testcase import ValidatorTestCase


class TestStringValidator(ValidatorTestCase):
  
  def test_it_validates_type(self):
    self.assertValidationPasses('banana', schema.string)
    self.assertValidationPasses('',       schema.string)

    self.assertValidationFails(None,  schema.string)
    self.assertValidationFails(False, schema.string)
    self.assertValidationFails(0,     schema.string)
    self.assertValidationFails([],    schema.string)
    self.assertValidationFails({},    schema.string)

  def test_it_validates_value(self):
    self.assertValidationPasses('banana', schema.string('banana'))
    self.assertValidationPasses('',       schema.string(''))
    self.assertValidationPasses(' ',      schema.string(' '))

    self.assertValidationFails(None,     schema.string(''))
    self.assertValidationFails('banana', schema.string('cucumber'))
    self.assertValidationFails('',       schema.string(' '))
    self.assertValidationFails(' ',      schema.string(''))

  def test_it_validates_pattern(self):
    self.assertValidationPasses('banana', schema.string.pattern(r'^[a-z]+$'))

    self.assertValidationFails('banana', schema.string.pattern(r'^[0-9]+$'))

  def test_it_validates_alphabet(self):
    self.assertValidationPasses('id',     schema.string.alphabetic)
    self.assertValidationPasses('1234',   schema.string.numeric)
    self.assertValidationPasses('id1234', schema.string.alpha_num)
    self.assertValidationPasses('id',     schema.string.alphabetic.lowercase)
    self.assertValidationPasses('ID',     schema.string.alphabetic.uppercase)
    self.assertValidationPasses('id1234', schema.string.alpha_num.lowercase)
    self.assertValidationPasses('ID1234', schema.string.alpha_num.uppercase)

    self.assertValidationFails('1234',   schema.string.alphabetic)
    self.assertValidationFails('id',     schema.string.numeric)
    self.assertValidationFails(' ',      schema.string.alpha_num)
    self.assertValidationFails('ID',     schema.string.alphabetic.lowercase)
    self.assertValidationFails('id',     schema.string.alphabetic.uppercase)
    self.assertValidationFails('ID1234', schema.string.alpha_num.lowercase)
    self.assertValidationFails('id1234', schema.string.alpha_num.uppercase)

  def test_it_validates_length(self):
    self.assertValidationPasses('',   schema.string.empty)
    self.assertValidationPasses(' ',  schema.string.non_empty)
    self.assertValidationPasses('',   schema.string.length(0))
    self.assertValidationPasses('a',  schema.string.length(1))
    self.assertValidationPasses('a',  schema.string.length(1, 2))
    self.assertValidationPasses('ab', schema.string.length(1, 2))

    self.assertValidationFails(' ',  schema.string.empty)
    self.assertValidationFails('',   schema.string.non_empty)
    self.assertValidationFails(' ',  schema.string.length(0))
    self.assertValidationFails('a',  schema.string.length(2))
    self.assertValidationFails('ab', schema.string.length(0, 1))
    self.assertValidationFails('ab', schema.string.length(3, 5))

  def test_it_validates_nullable(self):
    self.assertValidationPasses(None, schema.string.nullable)
    self.assertValidationPasses(None, schema.string('banana').nullable)

    self.assertValidationFails(False, schema.string.nullable)
    self.assertValidationFails(0,     schema.string.nullable)
    self.assertValidationFails([],    schema.string.nullable)
    self.assertValidationFails({},    schema.string.nullable)


if __name__ == '__main__':
  unittest.main()
