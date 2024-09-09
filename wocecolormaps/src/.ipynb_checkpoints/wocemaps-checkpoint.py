import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

### defining potential temperature color bar
cdict_potentialtemperature = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.0, 0.0),
        (0.2857142857142857, 0.37109375, 0.37109375),
        (0.42857142857142855, 0.6640625, 0.6640625),
        (0.5714285714285714, 0.93359375, 0.93359375),
        (0.7142857142857143, 0.8828125, 0.8828125),
        (0.8571428571428571, 0.83984375, 0.83984375),
        (1.0, 0.796875, 0.796875),
    ),
    "green": (
        (0.0, 0.54296875, 0.54296875),
        (0.14285714285714285, 0.6171875, 0.6171875),
        (0.2857142857142857, 0.71875, 0.71875),
        (0.42857142857142855, 0.84375, 0.84375),
        (0.5714285714285714, 0.71484375, 0.71484375),
        (0.7142857142857143, 0.48046875, 0.48046875),
        (0.8571428571428571, 0.28515625, 0.28515625),
        (1.0, 0.0, 0.0),
    ),
    "blue": (
        (0.0, 0.75390625, 0.75390625),
        (0.14285714285714285, 0.79296875, 0.79296875),
        (0.2857142857142857, 0.84375, 0.84375),
        (0.42857142857142855, 0.89453125, 0.89453125),
        (0.5714285714285714, 0.6640625, 0.6640625),
        (0.7142857142857143, 0.453125, 0.453125),
        (0.8571428571428571, 0.30859375, 0.30859375),
        (1.0, 0.20703125, 0.20703125),
    ),
}
potentialtemperature_woce = mpl.colors.LinearSegmentedColormap(
    "potentialtemperature_cmap", segmentdata=cdict_potentialtemperature
)

### defining salinity color bar
cdict_salinity = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.0, 0.0),
        (0.2857142857142857, 0.37109375, 0.37109375),
        (0.42857142857142855, 0.6640625, 0.6640625),
        (0.5714285714285714, 0.97265625, 0.97265625),
        (0.7142857142857143, 0.953125, 0.953125),
        (0.8571428571428571, 0.9296875, 0.9296875),
        (1.0, 0.90234375, 0.90234375),
    ),
    "green": (
        (0.0, 0.54296875, 0.54296875),
        (0.14285714285714285, 0.6171875, 0.6171875),
        (0.2857142857142857, 0.71875, 0.71875),
        (0.42857142857142855, 0.84375, 0.84375),
        (0.5714285714285714, 0.86328125, 0.86328125),
        (0.7142857142857143, 0.75390625, 0.75390625),
        (0.8571428571428571, 0.65625, 0.65625),
        (1.0, 0.55468, 0.55468),
    ),
    "blue": (
        (0.0, 0.75390625, 0.75390625),
        (0.14285714285714285, 0.79296875, 0.79296875),
        (0.2857142857142857, 0.84375, 0.84375),
        (0.42857142857142855, 0.89453125, 0.89453125),
        (0.5714285714285714, 0.71875, 0.71875),
        (0.7142857142857143, 0.53125, 0.53125),
        (0.8571428571428571, 0.3828125, 0.3828125),
        (1.0, 0.25, 0.25),
    ),
}

salinity_woce = mpl.colors.LinearSegmentedColormap(
    "salinity_woce", segmentdata=cdict_salinity
)

### defining neutral density color bar
cdict_neutraldensity = {
    "red": (
        (0.0, 0.796875, 0.796875),
        (0.14285714285714285, 0.83984375, 0.83984375),
        (0.2857142857142857, 0.8828125, 0.8828125),
        (0.42857142857142855, 0.93359375, 0.93359375),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.421875, 0.421875),
        (0.8571428571428571, 0.22265625, 0.22265625),
        (1.0, 0.00390625, 0.00390625),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.14285714285714285, 0.28515625, 0.28515625),
        (0.2857142857142857, 0.48046875, 0.48046875),
        (0.42857142857142855, 0.71484375, 0.71484375),
        (0.5714285714285714, 0.8046875, 0.8046875),
        (0.7142857142857143, 0.65625, 0.65625),
        (0.8571428571428571, 0.55078125, 0.55078125),
        (1.0, 0.45703125, 0.45703125),
    ),
    "blue": (
        (0.0, 0.20703125, 0.20703125),
        (0.14285714285714285, 0.30859375, 0.30859375),
        (0.2857142857142857, 0.453125, 0.453125),
        (0.42857142857142855, 0.6640625, 0.6640625),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.45703125, 0.45703125),
        (0.8571428571428571, 0.30078125, 0.30078125),
        (1.0, 0.1953125, 0.1953125),
    ),
}

neutraldensity_woce = mpl.colors.LinearSegmentedColormap(
    "neutraldensity_woce", segmentdata=cdict_neutraldensity
)

### defining potential density color bar
cdict_potentialdensity = {
    "red": ((0.0, 0.93359375, 0.93359375), (0.5, 0.421875, 0.421875), (1.0, 0.0, 0.0)),
    "green": (
        (0.0, 0.71484375, 0.71484375),
        (0.5, 0.65625, 0.65625),
        (1.0, 0.6171875, 0.6171875),
    ),
    "blue": (
        (0.0, 0.6640625, 0.6640625),
        (0.5, 0.45703125, 0.45703125),
        (1.0, 0.79296875, 0.79296875),
    ),
}

potentialdensity_woce = mpl.colors.LinearSegmentedColormap(
    "potentialdensity_woce", segmentdata=cdict_potentialdensity
)


### defining oxygen color bar
cdict_oxygen = {
    "red": (
        (0.0, 0.98046875, 0.98046875),
        (0.166666667, 0.96875, 0.96875),
        (0.333333333, 0.93359375, 0.93359375),
        (0.5, 0.8203125, 0.8203125),
        (0.666666667, 0.6953125, 0.6953125),
        (0.833333333, 0.59375, 0.59375),
        (1.0, 0.50390625, 0.50390625),
    ),
    "green": (
        (0.0, 0.90625, 0.90625),
        (0.166666667, 0.921875, 0.921875),
        (0.333333333, 0.92578125, 0.92578125),
        (0.5, 0.71875, 0.71875),
        (0.666666667, 0.5078125, 0.5078125),
        (0.833333333, 0.3359375, 0.3359375),
        (1.0, 0.19921875, 0.19921875),
    ),
    "blue": (
        (0.0, 0.246093755, 0.246093755),
        (0.166666667, 0.51171875, 0.51171875),
        (0.333333333, 0.734375, 0.734375),
        (0.5, 0.765625, 0.765625),
        (0.666666667, 0.66015625, 0.66015625),
        (0.833333333, 0.54296875, 0.54296875),
        (1.0, 0.48046875, 0.48046875),
    ),
}

oxygen_woce = mpl.colors.LinearSegmentedColormap(
    "oxygen_woce", segmentdata=cdict_oxygen
)


### defining phosphate color bar
cdict_phosphate = {
    "red": (
        (0.0, 0.90234375, 0.90234375),
        (0.14285714285714285, 0.9296875, 0.9296875),
        (0.2857142857142857, 0.953125, 0.953125),
        (0.42857142857142855, 0.97265625, 0.97265625),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.421875, 0.421875),
        (0.8571428571428571, 0.22265625, 0.22265625),
        (1.0, 0.00390625, 0.00390625),
    ),
    "green": (
        (0.0, 0.5546875, 0.5546875),
        (0.14285714285714285, 0.65625, 0.65625),
        (0.2857142857142857, 0.75390625, 0.75390625),
        (0.42857142857142855, 0.86328125, 0.86328125),
        (0.5714285714285714, 0.8046875, 0.8046875),
        (0.7142857142857143, 0.65625, 0.65625),
        (0.8571428571428571, 0.55078125, 0.55078125),
        (1.0, 0.45703125, 0.45703125),
    ),
    "blue": (
        (0.0, 0.25, 0.25),
        (0.14285714285714285, 0.3828125, 0.3828125),
        (0.2857142857142857, 0.53125, 0.53125),
        (0.42857142857142855, 0.71875, 0.71875),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.45703125, 0.45703125),
        (0.8571428571428571, 0.30078125, 0.30078125),
        (1.0, 0.1953125, 0.1953125),
    ),
}

phosphate_woce = mpl.colors.LinearSegmentedColormap(
    "phosphate_woce", segmentdata=cdict_phosphate
)

### defining nitrate color bar
cdict_nitrate = {
    "red": (
        (0.0, 0.0, 0.0),
        (0.142857143, 0.27734375, 0.27734375),
        (0.285714286, 0.48828125, 0.48828125),
        (0.428571429, 0.734375, 0.734375),
        (0.571428571, 0.8203125, 0.8203125),
        (0.714285714, 0.6953125, 0.6953125),
        (0.857142857, 0.59375, 0.59375),
        (1.0, 0.50390625, 0.50390625),
    ),
    "green": (
        (0.0, 0.53125, 0.53125),
        (0.142857143, 0.6171875, 0.6171875),
        (0.285714286, 0.70703125, 0.70703125),
        (0.428571429, 0.8359375, 0.8359375),
        (0.571428571, 0.7265625, 0.7265625),
        (0.714285714, 0.5078125, 0.5078125),
        (0.857142857, 0.3359375, 0.3359375),
        (1.0, 0.19921875, 0.19921875),
    ),
    "blue": (
        (0.0, 0.28125, 0.28125),
        (0.142857143, 0.375, 0.375),
        (0.285714286, 0.5234375, 0.5234375),
        (0.428571429, 0.72265625, 0.72265625),
        (0.571428571, 0.765625, 0.765625),
        (0.714285714, 0.66015625, 0.66015625),
        (0.857142857, 0.54296875, 0.54296875),
        (1.0, 0.48046875, 0.48046875),
    ),
}

nitrate_woce = mpl.colors.LinearSegmentedColormap(
    "nitrate_woce", segmentdata=cdict_nitrate
)


### defining silicate color bar
cdict_silicate = {
    "red": (
        (0.0, 0.99609375, 0.99609375),
        (0.14285714285714285, 0.99609375, 0.99609375),
        (0.2857142857142857, 0.99609375, 0.99609375),
        (0.42857142857142855, 0.99609375, 0.99609375),
        (0.5714285714285714, 0.93359375, 0.93359375),
        (0.7142857142857143, 0.8828125, 0.8828125),
        (0.8571428571428571, 0.83984375, 0.83984375),
        (1.0, 0.796875, 0.796875),
    ),
    "green": (
        (0.0, 0.94140625, 0.94140625),
        (0.14285714285714285, 0.9453125, 0.9453125),
        (0.2857142857142857, 0.96484375, 0.96484375),
        (0.42857142857142855, 0.98046875, 0.98046875),
        (0.5714285714285714, 0.71484375, 0.71484375),
        (0.7142857142857143, 0.48046875, 0.48046875),
        (0.8571428571428571, 0.28515625, 0.28515625),
        (1.0, 0.0, 0.0),
    ),
    "blue": (
        (0.0, 0.046875, 0.046875),
        (0.14285714285714285, 0.32421875, 0.32421875),
        (0.2857142857142857, 0.53125, 0.53125),
        (0.42857142857142855, 0.7421875, 0.7421875),
        (0.5714285714285714, 0.6640625, 0.6640625),
        (0.7142857142857143, 0.453125, 0.453125),
        (0.8571428571428571, 0.30859375, 0.30859375),
        (1.0, 0.20703125, 0.20703125),
    ),
}

silicate_woce = mpl.colors.LinearSegmentedColormap(
    "silicate_woce", segmentdata=cdict_silicate
)


### defining alkalinity color bar
cdict_alkalinity = {
    "red": (
        (0.0, 0.41796875, 0.41796875),
        (0.14285714285714285, 0.51953125, 0.51953125),
        (0.2857142857142857, 0.625, 0.625),
        (0.42857142857142855, 0.7734375, 0.7734375),
        (0.5714285714285714, 0.97265625, 0.97265625),
        (0.7142857142857143, 0.953125, 0.953125),
        (0.8571428571428571, 0.9296875, 0.9296875),
        (1.0, 0.90234375, 0.90234375),
    ),
    "green": (
        (0.0, 0.1015625, 0.1015625),
        (0.14285714285714285, 0.25, 0.25),
        (0.2857142857142857, 0.421875, 0.421875),
        (0.42857142857142855, 0.671875, 0.671875),
        (0.5714285714285714, 0.86328125, 0.86328125),
        (0.7142857142857143, 0.75390625, 0.75390625),
        (0.8571428571428571, 0.65625, 0.65625),
        (1.0, 0.5546875, 0.5546875),
    ),
    "blue": (
        (0.0, 0.41015625, 0.41015625),
        (0.14285714285714285, 0.50390625, 0.50390625),
        (0.2857142857142857, 0.61328125, 0.61328125),
        (0.42857142857142855, 0.77734375, 0.77734375),
        (0.5714285714285714, 0.71875, 0.71875),
        (0.7142857142857143, 0.53125, 0.53125),
        (0.8571428571428571, 0.3828125, 0.3828125),
        (1.0, 0.25, 0.25),
    ),
}

alkalinity_woce = mpl.colors.LinearSegmentedColormap(
    "alkalinity_woce", segmentdata=cdict_alkalinity
)


### defining total co2 color bar
cdict_totalco2 = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.0, 0.0),
        (0.2857142857142857, 0.37109375, 0.37109375),
        (0.42857142857142855, 0.6640625, 0.6640625),
        (0.5714285714285714, 0.99609375, 0.99609375),
        (0.7142857142857143, 0.99609375, 0.99609375),
        (0.8571428571428571, 0.99609375, 0.99609375),
        (1.0, 0.99609375, 0.99609375),
    ),
    "green": (
        (0.0, 0.54296875, 0.54296875),
        (0.14285714285714285, 0.6171875, 0.6171875),
        (0.2857142857142857, 0.71875, 0.71875),
        (0.42857142857142855, 0.84375, 0.84375),
        (0.5714285714285714, 0.98046875, 0.98046875),
        (0.7142857142857143, 0.96484375, 0.96484375),
        (0.8571428571428571, 0.9453125, 0.9453125),
        (1.0, 0.94140625, 0.94140625),
    ),
    "blue": (
        (0.0, 0.75390625, 0.75390625),
        (0.14285714285714285, 0.79296875, 0.79296875),
        (0.2857142857142857, 0.84375, 0.84375),
        (0.42857142857142855, 0.89453125, 0.89453125),
        (0.5714285714285714, 0.7421875, 0.7421875),
        (0.7142857142857143, 0.53125, 0.53125),
        (0.8571428571428571, 0.32421875, 0.32421875),
        (1.0, 0.046875, 0.046875),
    ),
}

totalco2_woce = mpl.colors.LinearSegmentedColormap(
    "totalco2_woce", segmentdata=cdict_totalco2
)


### defining cfc11 color bar
cdict_cfc11 = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.08984375, 0.08984375),
        (0.2857142857142857, 0.40234375, 0.40234375),
        (0.42857142857142855, 0.6796875, 0.6796875),
        (0.5714285714285714, 0.93359375, 0.93359375),
        (0.7142857142857143, 0.87890625, 0.87890625),
        (0.8571428571428571, 0.83984375, 0.83984375),
        (1.0, 0.79296875, 0.79296875),
    ),
    "green": (
        (0.0, 0.5546875, 0.5546875),
        (0.14285714285714285, 0.6328125, 0.6328125),
        (0.2857142857142857, 0.7265625, 0.7265625),
        (0.42857142857142855, 0.84765625, 0.84765625),
        (0.5714285714285714, 0.7265625, 0.7265625),
        (0.7142857142857143, 0.484375, 0.484375),
        (0.8571428571428571, 0.28515625, 0.28515625),
        (1.0, 0.0, 0.0),
    ),
    "blue": (
        (0.0, 0.421875, 0.421875),
        (0.14285714285714285, 0.51953125, 0.51953125),
        (0.2857142857142857, 0.640625, 0.640625),
        (0.42857142857142855, 0.78125, 0.78125),
        (0.5714285714285714, 0.796875, 0.796875),
        (0.7142857142857143, 0.6484375, 0.6484375),
        (0.8571428571428571, 0.53515625, 0.53515625),
        (1.0, 0.41796875, 0.41796875),
    ),
}

cfc11_woce = mpl.colors.LinearSegmentedColormap("cfc11_woce", segmentdata=cdict_cfc11)


### defining tritium color bar
cdict_tritium = {
    "red": (
        (0.0, 0.99609375, 0.99609375),
        (0.14285714285714285, 0.99609375, 0.99609375),
        (0.2857142857142857, 0.99609375, 0.99609375),
        (0.42857142857142855, 0.99609375, 0.99609375),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.421875, 0.421875),
        (0.8571428571428571, 0.22265625, 0.22265625),
        (1.0, 0.00390625, 0.00390625),
    ),
    "green": (
        (0.0, 0.94140625, 0.94140625),
        (0.14285714285714285, 0.9453125, 0.9453125),
        (0.2857142857142857, 0.96484375, 0.96484375),
        (0.42857142857142855, 0.98046875, 0.98046875),
        (0.5714285714285714, 0.8046875, 0.8046875),
        (0.7142857142857143, 0.65625, 0.65625),
        (0.8571428571428571, 0.55078125, 0.55078125),
        (1.0, 0.45703125, 0.45703125),
    ),
    "blue": (
        (0.0, 0.046875, 0.046875),
        (0.14285714285714285, 0.32421875, 0.32421875),
        (0.2857142857142857, 0.53125, 0.53125),
        (0.42857142857142855, 0.7421875, 0.7421875),
        (0.5714285714285714, 0.671875, 0.671875),
        (0.7142857142857143, 0.45703125, 0.45703125),
        (0.8571428571428571, 0.30078125, 0.30078125),
        (1.0, 0.1953125, 0.1953125),
    ),
}

tritium_woce = mpl.colors.LinearSegmentedColormap(
    "tritium_woce", segmentdata=cdict_tritium
)


### defining d3he color bar
cdict_d3he = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.22265625, 0.22265625),
        (0.2857142857142857, 0.421875, 0.421875),
        (0.42857142857142855, 0.671875, 0.671875),
        (0.5714285714285714, 0.6640625, 0.6640625),
        (0.7142857142857143, 0.37109375, 0.37109375),
        (0.8571428571428571, 0.0, 0.0),
        (1.0, 0.00390625, 0.00390625),
    ),
    "green": (
        (0.0, 0.45703125, 0.45703125),
        (0.14285714285714285, 0.55078125, 0.55078125),
        (0.2857142857142857, 0.65625, 0.65625),
        (0.42857142857142855, 0.8046875, 0.8046875),
        (0.5714285714285714, 0.84375, 0.84375),
        (0.7142857142857143, 0.71875, 0.71875),
        (0.8571428571428571, 0.6171875, 0.6171875),
        (1.0, 0.54296875, 0.54296875),
    ),
    "blue": (
        (0.0, 0.1953125, 0.1953125),
        (0.14285714285714285, 0.30078125, 0.30078125),
        (0.2857142857142857, 0.45703125, 0.45703125),
        (0.42857142857142855, 0.671875, 0.671875),
        (0.5714285714285714, 0.89453125, 0.89453125),
        (0.7142857142857143, 0.84375, 0.84375),
        (0.8571428571428571, 0.79296875, 0.79296875),
        (1.0, 0.75390625, 0.75390625),
    ),
}

d3he_woce = mpl.colors.LinearSegmentedColormap("d3he_woce", segmentdata=cdict_d3he)


### defining d14c color bar
cdict_d14c = {
    "red": (
        (0.0, 0.00390625, 0.00390625),
        (0.14285714285714285, 0.22265625, 0.22265625),
        (0.2857142857142857, 0.421875, 0.421875),
        (0.42857142857142855, 0.671875, 0.671875),
        (0.5714285714285714, 0.93359375, 0.93359375),
        (0.7142857142857143, 0.87890625, 0.87890625),
        (0.8571428571428571, 0.83984375, 0.83984375),
        (1.0, 0.79296875, 0.79296875),
    ),
    "green": (
        (0.0, 0.45703125, 0.45703125),
        (0.14285714285714285, 0.55078125, 0.55078125),
        (0.2857142857142857, 0.65625, 0.65625),
        (0.42857142857142855, 0.8046875, 0.8046875),
        (0.5714285714285714, 0.7265625, 0.7265625),
        (0.7142857142857143, 0.484375, 0.484375),
        (0.8571428571428571, 0.28515625, 0.28515625),
        (1.0, 0.0, 0.0),
    ),
    "blue": (
        (0.0, 0.1953125, 0.1953125),
        (0.14285714285714285, 0.30078125, 0.30078125),
        (0.2857142857142857, 0.45703125, 0.45703125),
        (0.42857142857142855, 0.671875, 0.671875),
        (0.5714285714285714, 0.796875, 0.796875),
        (0.7142857142857143, 0.6484375, 0.6484375),
        (0.8571428571428571, 0.53515625, 0.53515625),
        (1.0, 0.41796875, 0.41796875),
    ),
}

d14c_woce = mpl.colors.LinearSegmentedColormap("d14c_woce", segmentdata=cdict_d14c)


### defining depth color bar
cdict_depth = {
    "red": (
        (0.0, 0.79296875, 0.79296875),
        (0.14285714285714285, 0.859375, 0.859375),
        (0.2857142857142857, 0.99609375, 0.99609375),
        (0.42857142857142855, 0.4140625, 0.4140625),
        (0.5714285714285714, 0.0, 0.0),
        (0.7142857142857143, 0.00390625, 0.00390625),
        (0.8571428571428571, 0.12890625, 0.12890625),
        (1.0, 0.41015625, 0.41015625),
    ),
    "green": (
        (0.0, 0.09765625, 0.09765625),
        (0.14285714285714285, 0.47265625, 0.47265625),
        (0.2857142857142857, 0.94140625, 0.94140625),
        (0.42857142857142855, 0.7109375, 0.7109375),
        (0.5714285714285714, 0.6171875, 0.6171875),
        (0.7142857142857143, 0.4375, 0.4375),
        (0.8571428571428571, 0.14453125, 0.14453125),
        (
            1.0,
            0.12890625,
            0.12890625,
        ),
    ),
    "blue": (
        (0.0, 0.15234375, 0.15234375),
        (0.14285714285714285, 0.1796875, 0.1796875),
        (0.2857142857142857, 0.046875, 0.046875),
        (0.42857142857142855, 0.4609375, 0.4609375),
        (0.5714285714285714, 0.83984375, 0.83984375),
        (0.7142857142857143, 0.68359375, 0.68359375),
        (0.8571428571428571, 0.421875, 0.421875),
        (1.0, 0.42578125, 0.42578125),
    ),
}

depth_woce = mpl.colors.LinearSegmentedColormap("depth_woce", segmentdata=cdict_depth)


### Important notes
###these colormaps cannot be reversed
###The 'under' label is given to the lower value while the 'over' label is given to the higher value
