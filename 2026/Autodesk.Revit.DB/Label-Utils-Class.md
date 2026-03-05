# Label Utils Class

Source: https://www.revitapidocs.com/2026/39d096e3-6f2f-13ac-237b-7549d9841ef5.htm

---

| Label Utils Class |
| --- |

Used to obtain user\-visible names for enums. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB LabelUtils 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class LabelUtils : IDisposable
```

```
Public Class LabelUtils
	Implements IDisposable
```

```
public ref class LabelUtils : IDisposable
```

```
type LabelUtils = 
    class
        interface IDisposable
    end
```
The LabelUtils type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](06f80896-f874-197e-53a4-022263eeea91.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](68b266bc-631e-fc0e-2d8f-e0b03ad72ec7.htm) | Releases all resources used by the LabelUtils |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetFailureSeverityName](Label-Utils-Get-Failure-Severity-Name-Method.md) | Gets the user\-visible name for the Severity of a Warning |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(BuiltInCategory)](3c5057a7-b59e-c650-0d46-643f3bae218d.htm) | Gets the user\-visible name for a BuiltInCategory. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(BuiltInParameter)](ca0f955c-7cfa-e894-c0bc-dfa269aae5b4.htm) | Gets the user\-visible name for a BuiltInParameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(BuiltInParameter, LanguageType)](c38e7823-31b3-9bcd-5ab0-d353e0d39fa8.htm) | Gets the user\-visible name for a BuiltInParameter in a specific LanguageType. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(DuctLossMethodType, Document)](42396276-236f-3d66-84af-877397c4b08b.htm) | Gets the user\-visible name for a DuctLossMethodType. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(gbXMLBuildingType, Document)](Label-Utils-Get-Label-For-gb-XMLBuilding-Type-Document-Method.md) | Gets the user\-visible name for a gbXMLBuildingType. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(PipeFlowState, Document)](0fcc9faa-4526-622c-924e-5dad5c61c228.htm) | Gets the user\-visible name for a PipeFlowState. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelFor(PipeLossMethodType, Document)](fa0a0158-ecdc-0557-4214-14d5917d8c67.htm) | Gets the user\-visible name for a PipeLossMethodType. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForBuiltInParameter(ForgeTypeId)](482c49db-8994-bcc8-3077-02d8f40ba3db.htm) | Gets the user\-visible name for a built\-in parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForBuiltInParameter(ForgeTypeId, LanguageType)](c823565b-b71f-cc64-597a-eed82de7106f.htm) | Gets the user\-visible name for a built\-in parameter in a specific LanguageType. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForDiscipline](Label-Utils-Get-Label-For-Discipline-Method.md) | Gets the user\-visible name for a discipline. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForGroup](fad046bf-b6c9-35cd-69f2-1d556ddbbc05.htm) | Gets the user\-visible name for a built\-in parameter group. To get the name of parameter group "Other", pass an empty, default\-constructed ForgeTypeId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForSpec](Label-Utils-Get-Label-For-Spec-Method.md) | Gets the user\-visible name for a spec. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForSymbol](Label-Utils-Get-Label-For-Symbol-Method.md) | Gets the user\-visible name for a symbol. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetLabelForUnit](Label-Utils-Get-Label-For-Unit-Method.md) | Gets the user\-visible name for a unit. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetStructuralSectionShapeName](Label-Utils-Get-Structural-Section-Shape-Name-Method.md) | Gets the user\-visible name for a StructuralSectionShape. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
