"""
ASDF tags for spectroscopy related models.
"""

import numpy as np
from numpy.testing import assert_array_equal
from asdf import yamlutil
from ..gwcs_types import GWCSTransformType
from .. spectroscopy import *
from . import _parameter_to_value


__all__ = ['SellmeierGlassType', 'SellmeierZemaxType', 'Snell3D']


class SellmeierGlassType(GWCSTransformType):
    name = "sellmeier_glass"
    types = [SellmeierGlass]
    version = "1.0.0"

    @classmethod
    def from_tree_transform(cls, node, ctx):
        return SellmeierGlass(node['B_coef'], node['C_coef'])

    @classmethod
    def to_tree_transform(cls, model, ctx):
        node = {'B_coef': _parameter_to_value(model.B_coef),
                'C_coef': _parameter_to_value(model.C_coef)}
        return yamlutil.custom_tree_to_tagged_tree(node, ctx)


class SellmeierZemaxType(GWCSTransformType):
    name = "sellmeier_zemax"
    types = [SellmeierZemax]
    version = "1.0.0"

    @classmethod
    def from_tree_transform(cls, node, ctx):
        return SellmeierZemax(node['temperature'], node['ref_temperature'],
                              node['ref_pressure'], node['pressure'],
                              node['B_coef'], node['C_coef'], node['D_coef'],
                              node['E_coef'])

    @classmethod
    def to_tree_transform(cls, model, ctx):
        node = {'B_coef': _parameter_to_value(model.B_coef),
                'C_coef': _parameter_to_value(model.C_coef),
                'D_coef': _parameter_to_value(model.D_coef),
                'E_coef': _parameter_to_value(model.E_coef),
                'temperature': _parameter_to_value(model.temperature),
                'ref_temperature': _parameter_to_value(model.ref_temperature),
                'pressure': _parameter_to_value(model.pressure),
                'ref_pressure': _parameter_to_value(model.ref_pressure)}
        return yamlutil.custom_tree_to_tagged_tree(node, ctx)


class Snell3DType(GWCSTransformType):
    name = "snell3d"
    types = [Snell3D]
    version = "1.0.0"

    @classmethod
    def from_tree_transform(cls, node, ctx):
        return Snell3D()

    @classmethod
    def to_tree_transform(cls, model, ctx):
        return yamlutil.custom_tree_to_tagged_tree({}, ctx)