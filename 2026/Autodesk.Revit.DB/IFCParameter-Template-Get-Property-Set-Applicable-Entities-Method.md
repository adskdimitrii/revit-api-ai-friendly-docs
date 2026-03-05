# IFCParameter Template Get Property Set Applicable Entities Method

Source: https://www.revitapidocs.com/2026/2dda474c-3a64-4361-5b0b-b91d5066ea7b.htm

---

| IFCParameter Template Get Property Set Applicable Entities Method |
| --- |

Gets the list of IFC entities to which the property set is applicable. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<string> GetPropertySetApplicableEntities(
	PropertySetupType propertySetupType,
	string propertySetName
)
```

```
Public Function GetPropertySetApplicableEntities ( 
	propertySetupType As PropertySetupType,
	propertySetName As String
) As IList(Of String)
```

```
public:
IList<String^>^ GetPropertySetApplicableEntities(
	PropertySetupType propertySetupType, 
	String^ propertySetName
)
```

```
member GetPropertySetApplicableEntities : 
        propertySetupType : PropertySetupType * 
        propertySetName : string -> IList<string> 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

#### Return Value

IList String 
The list of IFC entities to which the property set is applicable. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A property set with the given name is not present in the template. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
