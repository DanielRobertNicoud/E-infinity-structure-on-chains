import setuptools

long_description = """
Computation of the E-infinity structure on normalized chains following
"Combinatorial operad actions on cochains" by Berger-Fresse.

Please find the full package documentation in the original Github repository_.

|
|

+---------+-------------------------------------------------------------------+
| Version | Comments                                                          |
+=========+===================================================================+
| 0.0.0   | First version.                                         |
+---------+-------------------------------------------------------------------+

.. _repository: https://github.com/DanielRobertNicoud/dupont-contraction
"""

setuptools.setup(
    name='e-infinity-chains',
    version='0.0.0',
    author='Daniel Robert-Nicoud',
    author_email='daniel.robertnicoud@gmail.com',
    description=(
        "Computation of the E-infinity structure on normalized chains"
        "following 'Combinatorial operad actions on cochains' by"
        " Berger-Fresse."
        ),
    long_description=long_description,
    url='https://github.com/DanielRobertNicoud/dupont-contraction',
    install_requires=[],
    packages=setuptools.find_packages(),
    namespace_packages=['eoo']
)
