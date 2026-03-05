# Rebar Crank Overridable Parameters Class

Source: https://www.revitapidocs.com/2026/739a340c-33c6-5afc-5dab-e7a0f2b75a49.htm

---

| Rebar Crank Overridable Parameters Class |
| --- |

Class used to store the formula parameter ids defined in the RebarShape family which are associated with crank length, crank offset length, crank straight length and crank angled length parameters. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarCrankOverridableParameters 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarCrankOverridableParameters : IDisposable
```

```
Public Class RebarCrankOverridableParameters
	Implements IDisposable
```

```
public ref class RebarCrankOverridableParameters : IDisposable
```

```
type RebarCrankOverridableParameters = 
    class
        interface IDisposable
    end
```
The RebarCrankOverridableParameters type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](Rebar-Crank-Overridable-Parameters-Is-Valid-Object-Property.md) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](Rebar-Crank-Overridable-Parameters-Dispose-Method.md) | Releases all resources used by the RebarCrankOverridableParameters |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankEndAngledLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-End-Angled-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with end crank angled length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankEndLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-End-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with end crank length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankEndOffsetLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-End-Offset-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with end crank offset length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankEndRatioFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-End-Ratio-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with end crank ratio parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankEndStraightLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-End-Straight-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with end crank straight length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankStartAngledLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-Start-Angled-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with start crank angled length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankStartLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-Start-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with start crank length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankStartOffsetLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-Start-Offset-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with start crank offset length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankStartRatioFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-Start-Ratio-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with start crank ratio parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankStartStraightLengthFormulaParams](Rebar-Crank-Overridable-Parameters-Get-Crank-Start-Straight-Length-Formula-Params-Method.md) | Gets the formula parameter ids defined in the RebarShape family which are associated with start crank straight length parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
