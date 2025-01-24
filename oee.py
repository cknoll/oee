import pyirk as p

__URI__ = "irk:/oee/0.1"
keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# TOP-LEVEL CONCEPTS
I1101 = p.create_item(
    R1__has_label="physical quantity",
    R2__has_description="A fundamental quantity that can be measured and expressed in terms of units, such as length, mass, time, current, voltage, etc.",
    R4__is_instance_of=p.I2["Metaclass"],
    R18__has_usage_hint=(
        "Items such as 'voltage' or 'time' should be R4__is_instance_of-related to this item."
    )
)

I110101 = p.create_item(
    R1__has_label="Electric Current",
    R2__has_description="The flow of electric charge through a conductor.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110102 = p.create_item(
    R1__has_label="Voltage",
    R2__has_description="The difference in electric potential between two points in a circuit.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110103 = p.create_item(
    R1__has_label="Resistance",
    R2__has_description="The opposition to the flow of electric current in a conductor.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110104 = p.create_item(
    R1__has_label="Capacitance",
    R2__has_description="The ability of a component or system to store an electric charge.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110105 = p.create_item(
    R1__has_label="Inductance",
    R2__has_description="The property of a conductor that opposes changes in current.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110106 = p.create_item(
    R1__has_label="Power",
    R2__has_description="The rate at which electrical energy is converted into another form of energy.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110107 = p.create_item(
    R1__has_label="Energy",
    R2__has_description="The capacity to do work or transfer heat.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110108 = p.create_item(
    R1__has_label="Charge",
    R2__has_description="The quantity of electricity that is transported in an electric current.",
    R4__is_instance_of=I1101["physical quantity"]
)

I110109 = p.create_item(
    R1__has_label="Conductance",
    R2__has_description="The ability of a conductor to allow current to flow through it (inverse of resistance).",
    R4__is_instance_of=I1101["physical quantity"]
)

I110110 = p.create_item(
    R1__has_label="Impedance",
    R2__has_description="The total opposition to the flow of current in an alternating current (AC) circuit, including both resistance and reactance.",
    R4__is_instance_of=I1101["physical quantity"]
)



I1102 = p.create_item(
    R1__has_label="physical unit",
    R2__has_description="A unit of measurement used to quantify a physical quantity, such as the meter for length or the second for time.",
    R4__is_instance_of=p.I2["Metaclass"],
    R18__has_usage_hint="Items such as 'Volt' or 'second' should be R4__is_instance_of-related "
    "to this item or subclasses of it."
)


I110202 = p.create_item(
    R1__has_label="Volt",
    R2__has_description="The SI unit of electric potential difference (voltage).",
    R3__is_subclass_of=I1102["physical unit"]
)

I110203 = p.create_item(
    R1__has_label="Ohm",
    R2__has_description="The SI unit of electric resistance.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110204 = p.create_item(
    R1__has_label="Farad",
    R2__has_description="The SI unit of capacitance.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110205 = p.create_item(
    R1__has_label="Henry",
    R2__has_description="The SI unit of inductance.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110206 = p.create_item(
    R1__has_label="Watt",
    R2__has_description="The SI unit of power.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110207 = p.create_item(
    R1__has_label="Joule",
    R2__has_description="The SI unit of energy.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110208 = p.create_item(
    R1__has_label="Coulomb",
    R2__has_description="The SI unit of electric charge.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110209 = p.create_item(
    R1__has_label="Siemens",
    R2__has_description="The SI unit of electric conductance.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110210 = p.create_item(
    R1__has_label="Ohm",
    R2__has_description="The SI unit of impedance.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110211 = p.create_item(
    R1__has_label="Tesla",
    R2__has_description="The SI unit of magnetic flux density.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110212 = p.create_item(
    R1__has_label="Volt per meter",
    R2__has_description="The SI unit of electric field strength.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110213 = p.create_item(
    R1__has_label="Ampere per meter",
    R2__has_description="The SI unit of magnetic field strength.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110214 = p.create_item(
    R1__has_label="Hertz",
    R2__has_description="The SI unit of frequency.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110215 = p.create_item(
    R1__has_label="Meter",
    R2__has_description="The SI unit of wavelength.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110216 = p.create_item(
    R1__has_label="Farad per meter",
    R2__has_description="The SI unit of permittivity.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110217 = p.create_item(
    R1__has_label="Henry per meter",
    R2__has_description="The SI unit of permeability.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110218 = p.create_item(
    R1__has_label="Coulomb per square meter",
    R2__has_description="The SI unit of electric displacement.",
    R3__is_subclass_of=I1102["physical unit"]
)

I110219 = p.create_item(
    R1__has_label="Coulomb per square meter",
    R2__has_description="The SI unit of polarization.",
    R3__is_subclass_of=I1102["physical unit"]
)

I1103 = p.create_item(
    R1__has_label="SI unit",
    R2__has_description="class for units which are defined within the International System of Units",
    R3__is_subclass_of=I1102["physical unit"],
)

I1104 = p.create_item(
    R1__has_label="SI base unit",
    R2__has_description="class for units which are one of the seven base units defined within the "
    "International System of Units",
    R3__is_subclass_of=I1103["SI unit"],
    R72__is_generally_related_to="https://www.wikidata.org/wiki/Q12457",
)


I1201 = p.create_item(
    R1__has_label="second",
    R2__has_description="The SI base unit of time. It is defined as the duration of 9,192,631,770 periods of radiation corresponding to the transition between two hyperfine levels of the ground state of the cesium-133 atom.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1202 = p.create_item(
    R1__has_label="meter",
    R2__has_description="The SI base unit of length. It is defined as the distance that light travels in a vacuum in 1/299,792,458 seconds.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1203 = p.create_item(
    R1__has_label="kilogram",
    R2__has_description="The SI base unit of mass. It is defined as the mass of the international prototype of the kilogram, a platinum-iridium cylinder kept at the International Bureau of Weights and Measures.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1204 = p.create_item(
    R1__has_label="ampere",
    R2__has_description="The SI base unit of electric current. It is defined by taking the fixed numerical value of the elementary charge to be 1.602176634 × 10^-19 when expressed in coulombs.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1205 = p.create_item(
    R1__has_label="kelvin",
    R2__has_description="The SI base unit of thermodynamic temperature. It is defined as 1/273.16 of the thermodynamic temperature of the triple point of water.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1206 = p.create_item(
    R1__has_label="mole",
    R2__has_description="The SI base unit of the amount of substance. It is defined as the amount of substance that contains as many entities as there are atoms in 12 grams of carbon-12.",
    R4__is_instance_of=I1104["SI base unit"]
)

I1207 = p.create_item(
    R1__has_label="candela",
    R2__has_description="The SI base unit of luminous intensity. It is defined as the luminous intensity of a source that emits monochromatic radiation of frequency 540 × 10^12 hertz and has a radiant intensity of 1/683 watt per steradian.",
    R4__is_instance_of=I1104["SI base unit"]
)

# express that there are no more SI base units
p.close_class_with_R51(I1104["SI base unit"])



R1200 = p.create_relation(
    R1__has_label="has associated SI unit",
    R2__has_description="Specifies the SI unit which is uniquely associated to a physical "
    "quantity.",
    R8__has_domain_of_argument_1=I1101["physical quantity"],
    R11__has_range_of_result=I1103["SI unit"],
)


I1301 = p.create_item(
    R1__has_label="electrical current",
    R2__has_description="The flow of electric charge, typically measured in amperes. It is the rate at which charge flows through a conductor or circuit.",
    R4__is_instance_of=I1101["physical quantity"],
    R1200__has_associated_SI_unit=I1204["ampere"],
)


I1302 = p.create_item(
    R1__has_label="electrical voltage",
    R2__has_description="The difference in electric potential between two points in a circuit, typically measured in volts. It drives the flow of electric current.",
    R4__is_instance_of=I1101["physical quantity"],
    R1200__has_associated_SI_unit=I110202["Volt"]
)



## Statement number 1
## Current is the flow of electric charge in a circuit.

## Statement number 2
## Resistance opposes the flow of electric current in a circuit.

## Statement number 3
## A capacitor stores electrical energy in an electric field.

## Statement number 4
## An inductor stores energy in a magnetic field when current flows through it.

## Statement number 5
## Alternating current (AC) changes direction periodically, while direct current (DC) flows in one direction.

## Statement number 6
## Electrical circuits consist of components like resistors, capacitors, inductors, and power sources.

## Statement number 7
## Capacitance is the ability to store electric charge in a system when voltage is applied.

## Statement number 8
## Inductance is the ability of a coil or circuit to oppose changes in current by generating a voltage.


## Statement number 9














p.end_mod()


