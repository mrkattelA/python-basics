/*
This function calculates the monthly insurance premium for a single driver. 
The `driver` object is expected to have these properties:
    name: string
    ageInYears: number
    recentViolations: number: traffic violations received in the last 2 years
*/
function getMonthlyPremium(driver) {
    // Create a variable for the calculation
    let monthlyPremium;

    // Establish base rate by age
    if (driver.ageInYears < 26) {
        monthlyPremium = 130;
    } else if (driver.ageInYears > 65) {
        monthlyPremium = 115;
    } else {
        monthlyPremium = 100;
    }

    // Higher risk for citations in last two years
    monthlyPremium += driver.recentViolations * 25;

    return monthlyPremium;
}

/*
This function creates a quote for a family of drivers.
`family` is an array of drivers.
*/
function getFamilyAnnualQuote(family) {
    // Create a variable to sum up individual premiums
    let quote = 0;

    // Loop for each member of the family, and call getMonthlyPremium
    for(let i = 0; i < family.lenth; i++){
        let familyMember = family[i];
        let month = getMonthlyPremium(familyMember);
        // Display each member's monthly premium
        // Add the monthly premium * 12 to the total annual premium
        console.log("\tMonthly Premium for " + familyMember.name + ": $" + month);
        quote += month*12;
    }
    // Print the total to the console
    console.log("");//print a blank line
    console.log("Total Annual Premium: $" + quote)
    return quote;   

    
}

// Create the family array
let myFamily = [
    { name: 'Trudy', ageInYears: 52, recentViolations: 0 },
    { name: 'Maximillian', ageInYears: 48, recentViolations: 1 },
    { name: 'Aiden', ageInYears: 22, recentViolations: 0 },
    { name: 'Ki', ageInYears: 25, recentViolations: 3 }
]

getFamilyAnnualQuote(myFamily);

