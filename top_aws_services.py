import boto3
import matplotlib.pyplot as plt

# Initialize the Cost Explorer client
ce = boto3.client('ce')

# Function to get cost data
def get_cost_data(start_date, end_date):
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start_date, 'End': end_date},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )
    return response

# Function to process cost data
def process_cost_data(response):
    data = response['ResultsByTime'][0]['Groups']
    services = [item['Keys'][0] for item in data]
    costs = [float(item['Metrics']['UnblendedCost']['Amount']) for item in data]

    # Sort by cost and get top 5
    sorted_data = sorted(zip(services, costs), key=lambda x: x[1], reverse=True)[:5]
    return zip(*sorted_data)

# Generate the graph
def generate_graph(services, costs):
    plt.figure(figsize=(10, 6))
    plt.bar(services, costs, alpha=0.7)
    plt.title('Top 5 AWS Services by Cost', fontsize=16)
    plt.ylabel('Cost ($)', fontsize=14)
    plt.xlabel('Service', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('top_5_aws_services.png')
    plt.show()

# Main script
if __name__ == "__main__":

    start_date = '2024-11-01'  
    end_date = '2024-12-01'    

    print("Fetching cost data...")
    response = get_cost_data(start_date, end_date)

    print("Processing data...")
    services, costs = process_cost_data(response)

    print("Generating graph...")
    generate_graph(services, costs)

    print("Graph saved as 'top_5_aws_services.png'")
