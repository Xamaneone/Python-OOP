from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("My name", "Heavy", 500, 500)

    def test_attr_are_set(self):
        self.assertEqual("My name", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_has_no_memory__when_software_is_installed_raises(self):
        software = LightSoftware("S name", 501, 501)
        self.hardware.install(software)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_equal_capacity_and_memory_is_installed(self):
        software = LightSoftware("S name", 200, 1000)
        self.hardware.install(software)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_software_is_installed(self):
        software = LightSoftware("S name", 200, 500)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_unexisting_software_does_not_complain(self):
        software = LightSoftware("S name", 200, 500)
        self.assertEqual(0, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))


        #test data with some software
        software = LightSoftware("S name", 200, 500)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

        software_2 = LightSoftware("S222 name", 200, 500)
        self.assertNotIn(software_2, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software_2)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_software(self):
        software = LightSoftware("S name", 200, 500)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual([] ,self.hardware.software_components)





if __name__ == '__main__':
    main()