import unittest
from ansiblelint import RulesCollection, Runner
from ansiblelint.rules.MetaLicenseValidRule import MetaLicenseValidRule


class TestMetaLicenseValid(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(MetaLicenseValidRule())

    def test_license_valid(self):
        rolepath = 'test/role-meta-license-valid'
        runner = Runner(self.collection, rolepath, [], [], [])
        results = runner.run()
        self.assertEqual(results, [])

    def test_license_invalid(self):
        rolepath = 'test/role-meta-has-info'
        runner = Runner(self.collection, rolepath, [], [], [])
        results = runner.run()
        self.assertIn("Expected 'license' to be a valid SPDX license ID",
                      str(results[0]))
