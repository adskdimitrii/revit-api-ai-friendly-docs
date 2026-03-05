# IFCParameter Template Add Property Mapping Info Method

Source: https://www.revitapidocs.com/2026/93aecefe-55ff-6535-05f9-81043b56b0f2.htm

---

| IFCParameter Template Add Property Mapping Info Method |
| --- |

Adds a property mapping info to the property set. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddPropertyMappingInfo(
	PropertySetupType propertySetupType,
	string propertySetName,
	IFCPropertyMappingInfo propertyMappingInfo
)
```

```
Public Sub AddPropertyMappingInfo ( 
	propertySetupType As PropertySetupType,
	propertySetName As String,
	propertyMappingInfo As IFCPropertyMappingInfo
)
```

```
public:
void AddPropertyMappingInfo(
	PropertySetupType propertySetupType, 
	String^ propertySetName, 
	IFCPropertyMappingInfo^ propertyMappingInfo
)
```

```
member AddPropertyMappingInfo : 
        propertySetupType : PropertySetupType * 
        propertySetName : string * 
        propertyMappingInfo : IFCPropertyMappingInfo -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

propertyMappingInfo [IFCPropertyMappingInfo](IFCProperty-Mapping-Info-Class.md)
:   The property mapping info.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The mapping info is invalid.  \-or\-  A property set with the given name is not present in the template. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
