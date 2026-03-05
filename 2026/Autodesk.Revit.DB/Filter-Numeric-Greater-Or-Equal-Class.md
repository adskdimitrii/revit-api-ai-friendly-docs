# Filter Numeric Greater Or Equal Class

Source: https://www.revitapidocs.com/2026/c77b5955-2ca2-16aa-4567-5a4470e24289.htm

---

| Filter Numeric Greater Or Equal Class |
| --- |

Tests whether numeric values from the document are greater than or equal to a certain value ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB FilterNumericRuleEvaluator](Filter-Numeric-Rule-Evaluator-Class.md) 
Autodesk.Revit.DB FilterNumericGreaterOrEqual 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class FilterNumericGreaterOrEqual : FilterNumericRuleEvaluator
```

```
Public Class FilterNumericGreaterOrEqual
	Inherits FilterNumericRuleEvaluator
```

```
public ref class FilterNumericGreaterOrEqual : public FilterNumericRuleEvaluator
```

```
type FilterNumericGreaterOrEqual = 
    class
        inherit FilterNumericRuleEvaluator
    end
```
The FilterNumericGreaterOrEqual type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [FilterNumericGreaterOrEqual](ecd9943b-55bd-0e48-6e37-cd6ff45c7b52.htm) | Constructs an instance of FilterNumericGreaterOrEqual. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](109e70c2-5454-e1d9-f694-62560047bff2.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [FilterNumericRuleEvaluator](Filter-Numeric-Rule-Evaluator-Class.md) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](6726f509-1d75-7abb-cde6-bfbeebff2287.htm) | (Inherited from [FilterNumericRuleEvaluator](Filter-Numeric-Rule-Evaluator-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Evaluate(Int64, Int64\)](97c35e52-48cd-2581-aff3-c13556ea1af2.htm) | Derived classes should override this method to implement the desired test. (Inherited from [FilterNumericRuleEvaluator](Filter-Numeric-Rule-Evaluator-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Evaluate(Double, Double, Double)](4779f820-cb81-33f2-5dbf-91f257e76b3a.htm) | Derived classes override this method to implement the test that determines  whether the two given double\-precision values satisfy the desired condition or not. (Inherited from [FilterNumericRuleEvaluator](Filter-Numeric-Rule-Evaluator-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
