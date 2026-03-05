# Filter Numeric Rule Evaluator Class

Source: https://www.revitapidocs.com/2026/1f1a96bb-5f00-1a24-8c03-6984c88672b9.htm

---

| Filter Numeric Rule Evaluator Class |
| --- |

Base for all classes that compare numeric values from Revit to a user\-supplied filter value. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB FilterNumericRuleEvaluator 
[More](#fullInheritance) 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class FilterNumericRuleEvaluator : IDisposable
```

```
Public Class FilterNumericRuleEvaluator
	Implements IDisposable
```

```
public ref class FilterNumericRuleEvaluator : IDisposable
```

```
type FilterNumericRuleEvaluator = 
    class
        interface IDisposable
    end
```
The FilterNumericRuleEvaluator type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](109e70c2-5454-e1d9-f694-62560047bff2.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](6726f509-1d75-7abb-cde6-bfbeebff2287.htm) | Releases all resources used by the FilterNumericRuleEvaluator |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Evaluate(Int64, Int64\)](97c35e52-48cd-2581-aff3-c13556ea1af2.htm) | Derived classes should override this method to implement the desired test. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Evaluate(Double, Double, Double)](4779f820-cb81-33f2-5dbf-91f257e76b3a.htm) | Derived classes override this method to implement the test that determines  whether the two given double\-precision values satisfy the desired condition or not. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A class derived from FilterNumericRuleEvaluator must handle both integer and double\-precision types.
 For double\-precision comparisons, an epsilon value is given. The evaluator class should use this
 value in a manner appropriate to the comparison being implemented. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB FilterNumericRuleEvaluator 
[Autodesk.Revit.DB FilterNumericEquals](Filter-Numeric-Equals-Class.md) 
[Autodesk.Revit.DB FilterNumericGreater](Filter-Numeric-Greater-Class.md) 
[Autodesk.Revit.DB FilterNumericGreaterOrEqual](Filter-Numeric-Greater-Or-Equal-Class.md) 
[Autodesk.Revit.DB FilterNumericLess](Filter-Numeric-Less-Class.md) 
[Autodesk.Revit.DB FilterNumericLessOrEqual](Filter-Numeric-Less-Or-Equal-Class.md)
