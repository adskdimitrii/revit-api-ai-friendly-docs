# Document Link(String, Import Options 3DM, View) Method

Source: https://www.revitapidocs.com/2026/10dac8a0-bf4c-d238-9635-9b2aa58e156b.htm

---

| Document Link(String, Import Options 3DM, View) Method |
| --- |

Links a 3DM file into the project document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId Link(
	string file,
	ImportOptions3DM options,
	View pDBView
)
```

```
Public Function Link ( 
	file As String,
	options As ImportOptions3DM,
	pDBView As View
) As ElementId
```

```
public:
ElementId^ Link(
	String^ file, 
	ImportOptions3DM^ options, 
	View^ pDBView
)
```

```
member Link : 
        file : string * 
        options : ImportOptions3DM * 
        pDBView : View -> ElementId 
```

#### Parameters

file String
:   Full path of the file to link. File must exist and must be a valid 3DM file.

options [ImportOptions3DM](72310605-e939-bc8c-c790-642da4cc02cb.htm)
:   Various import options applicable to the 3DM format. If , all options will be set to their respective default values.

pDBView [View](View-Class.md)
:   View used to aid placement of the linked file. If the options specify ThisViewOnly, this argument is required and the linked file
 will only be visible in the specified view. If the options specify center\-to\-center placement, this argument is required and the linked
 file will be placed in the center of the specified view. Otherwise, this view is used to obtain a base level to associate with the linked
 file. If not specified, an existing view will be chosen instead and may open a view or associate the linked file to an arbitrary level.

#### Return Value

[ElementId](Element-Id-Class.md) 
Returns the element Id of the linked instance. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Not a valid file for 3DM import (.3dm files are valid).  \-or\-  ThisViewOnly cannot be true when importing a DWG\|DGN drawing into a 3D view.  \-or\-  The provided view is not valid for the options provided.  \-or\-  One or more strings describing layer selection is invalid or empty.  \-or\-  The scale is not valid as a CustomScale for use during import.  \-or\-  NullOrEmpty  \-or\-  The view is not printable. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given file does not exist. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Import is temporarily disabled.  \-or\-  This Document is not a project document. |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The Material Library is missing in the installed Revit.  \-or\-  The 3DM Import/Link module is not available in the installed Revit. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Link isn't supported for family documents. Please use import instead. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Link Overload](0e45b625-904e-06be-fabc-8591fed616f8.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
