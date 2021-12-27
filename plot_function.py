import base_function
import matplotlib.pyplot as plt

def plot_npv_profile(first_cash_flow, second_cash_flow):
    if second_cash_flow == [0,0]:
        first_irr, second_irr, diff_cash_flow_irr, df_npv = base_function.npv_profile(first_cash_flow, second_cash_flow)
        plt.figure(figsize=(9,6))

        plt.axhline(y=0, c='gray', linestyle='dashed')
        plt.axvline(x=diff_cash_flow_irr, c='gray', linestyle='dashed')

        plt.plot(df_npv['Discount Rate'], df_npv['Project A'], label='Project A')
        
        plt.title("NPV Profile (Sensitivity Test for NPV)", fontsize=14)
        plt.xlabel('Discount Rate (r)')
        plt.ylabel('NPV (in dollar)')
        plt.legend()
        plt.show()
    else:
        first_irr, second_irr, diff_cash_flow_irr, df_npv = base_function.npv_profile(first_cash_flow, second_cash_flow)
        plt.figure(figsize=(9,6))

        plt.axhline(y=0, c='gray', linestyle='dashed')
        plt.axvline(x=diff_cash_flow_irr, c='gray', linestyle='dashed')

        plt.plot(df_npv['Discount Rate'], df_npv['Project A'], label='Project A')
        plt.plot(df_npv['Discount Rate'], df_npv['Project B'], label='Project B')
        
        plt.title("NPV Profile (Sensitivity Test for NPV)", fontsize=14)
        plt.xlabel('Discount Rate (r)')
        plt.ylabel('NPV (in dollar)')
        plt.legend()
        plt.show()







if __name__ == '__main__':
    first_cash_flow = [-11000, 7000, 7500, 7000, 7000]
    second_cash_flow = [-150000, 80000, 80000, 30000, 10000, 20000]
    plot_npv_profile(first_cash_flow, second_cash_flow)
