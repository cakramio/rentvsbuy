import streamlit as st
import pandas as pd


def calculate_total_cost(data, years):
  """Calculates the total cost of buying or renting."""
  if "Purchase Price" in data.columns:
    # Buyinstreg cost
    total_cost = data["Purchase Price"] + \
      data["Down Payment"] + \
      (data["Property Tax"] + data["Maintenance"] + data["Mortgage Payment"]) * years
  else:
    # Renting cost
    total_cost = data["Monthly Rent"] * 12 * years

  return total_cost


def app():
  """Main function of the Streamlit app."""
  st.title("Rent vs Buy Model")

  # User input section
  st.subheader("Financial Assumptions")
  purchase_price = st.number_input("Purchase Price ($)", min_value=0.0)
  down_payment = st.number_input("Down Payment ($)", min_value=0.0)
  property_tax = st.number_input("Property Tax (%/year)", min_value=0.0)
  maintenance = st.number_input("Maintenance (%/year)", min_value=0.0)
  mortgage_rate = st.number_input("Mortgage Interest Rate (%/year)", min_value=0.0)
  monthly_rent = st.number_input("Monthly Rent ($)", min_value=0.0)
  years = st.number_input("Years of Ownership", min_value=1)
  mortgage_payment = 0

  # Calculate mortgage payment
  if purchase_price > 0:
    loan_amount = purchase_price - down_payment
    mortgage_payment = loan_amount * (mortgage_rate / (1 - (1 + mortgage_rate)**(-years)))

  # Create data dictionary
  data = {
      "Purchase Price": purchase_price,
      "Down Payment": down_payment,
      "Property Tax": property_tax / 100,
      "Maintenance": maintenance / 100,
      "Mortgage Payment": mortgage_payment,
      "Monthly Rent": monthly_rent,
  }

  # Calculate total costs
  rent_cost = calculate_total_cost(pd.DataFrame(data, index=[0]), years)
  buy_cost = calculate_total_cost(pd.DataFrame(data, index=[0]), years)

  # Display results
  st.subheader("Results")
  st.write(f"Total Cost of Renting for {years} years: ${rent_cost:.2f}")
  st.write(f"Total Cost of Buying for {years} years: ${buy_cost:.2f}")

  # Show difference
  cost_difference = buy_cost - rent_cost
  if cost_difference > 0:
    st.write(f"**Buying is ${cost_difference:.2f} more expensive than renting over {years} years.**")
  elif cost_difference < 0:
    st.write(f"**Buying is ${abs(cost_difference):.2f} cheaper than renting over {years} years.**")
  else:
    st.write(f"The total cost of buying and renting is equal over {years} years.")


if __name__ == "__main__":
  app()