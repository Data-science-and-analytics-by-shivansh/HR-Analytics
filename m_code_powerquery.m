let
    Source = Csv.Document(File.Contents("data/hr_analytics_data.csv")),
    #"Promoted Headers" = Table.PromoteHeaders(Source),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", {{"Age", Int64.Type}, {"MonthlyIncome", type number}, {"YearsAtCompany", Int64.Type}}),
    #"Added AttritionFlag" = Table.AddColumn(#"Changed Type", "AttritionFlag", each if [Attrition] = "Yes" then 1 else 0, Int64.Type),
    #"Added DiversityIndex" = Table.AddColumn(#"Added AttritionFlag", "DiversityIndex", each if [Gender] = "Female" then 1 else 0, Int64.Type)
in
    #"Added DiversityIndex"
