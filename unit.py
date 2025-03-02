
import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

def main():
    st.title("Unit Converter")

    options = ["Time", "Area", "Volume", "Temperature", "Weight", "Length"]
    choice = st.selectbox("Select conversion type", options)

    if choice == "Time":
        time_units = {"seconds": 1, "minutes": 60, "hours": 3600}
        from_unit = st.selectbox("From", list(time_units.keys()))
        to_unit = st.selectbox("To", list(time_units.keys()))
        value = st.number_input("Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_units(value, from_unit, to_unit, time_units)
            st.write(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == "Area":
        area_units = {"square meters": 1, "square kilometers": 1e6, "square miles": 2.59e6}
        from_unit = st.selectbox("From", list(area_units.keys()))
        to_unit = st.selectbox("To", list(area_units.keys()))
        value = st.number_input("Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_units(value, from_unit, to_unit, area_units)
            st.write(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == "Volume":
        volume_units = {"liters": 1, "milliliters": 0.001, "cubic meters": 1000}
        from_unit = st.selectbox("From", list(volume_units.keys()))
        to_unit = st.selectbox("To", list(volume_units.keys()))
        value = st.number_input("Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_units(value, from_unit, to_unit, volume_units)
            st.write(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == "Temperature":
        temp_units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
        from_unit = st.selectbox("From", list(temp_units.keys()))
        to_unit = st.selectbox("To", list(temp_units.keys()))
        value = st.number_input("Value", format="%.2f")
        if st.button("Convert"):
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
            st.write(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == "Weight":
        weight_units = {"grams": 1, "kilograms": 1000, "pounds": 453.592}
        from_unit = st.selectbox("From", list(weight_units.keys()))
        to_unit = st.selectbox("To", list(weight_units.keys()))
        value = st.number_input("Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_units(value, from_unit, to_unit, weight_units)
            st.write(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == "Length":
        length_units = {"meters": 1, "kilometers": 1000, "miles": 1609.34}
        from_unit = st.selectbox("From", list(length_units.keys()))
        to_unit = st.selectbox("To", list(length_units.keys()))
        value = st.number_input("Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_units(value, from_unit, to_unit, length_units)
            st.write(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == "__main__":
    main()
